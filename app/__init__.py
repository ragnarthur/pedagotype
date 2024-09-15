from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    # Carrega as variáveis de ambiente do .env
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Conexão com MongoDB
    mongo_url = os.getenv('MONGO_URL')
    mongo_database = os.getenv('MONGO_DATABASE')
    
    # Verifica se as variáveis de ambiente são válidas
    if not mongo_url or not mongo_database:
        raise ValueError("MONGO_URL ou MONGO_DATABASE não estão definidos nas variáveis de ambiente.")
    
    # Conecta ao MongoDB
    mongo = MongoClient(mongo_url)
    db = mongo[mongo_database]

    # Passa o db via configuração global
    app.config['db'] = db

    # Filtro para converter quebras de linha em <br> no HTML
    @app.template_filter('nl2br')
    def nl2br_filter(s):
        return s.replace("\n", "<br>\n")

    # Importar as rotas
    from .routes import main
    from .auth import auth
    from .api import api  # Certifique-se de importar o blueprint 'api'

    # Registrar blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(api)  # Registrar o blueprint 'api'

    return app
