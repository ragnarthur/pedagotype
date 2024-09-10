import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Conexão com MongoDB
    mongo_url = os.getenv('MONGO_URL')
    mongo_database = os.getenv('MONGO_DATABASE')
    
    mongo = MongoClient(mongo_url)
    db = mongo[mongo_database]

    # Importar e registrar blueprints após a criação do app
    from .routes import main
    from .api import api  # A importação do api.py vem aqui

    # Usar um contexto global para o db no app
    app.config['db'] = db  # Passa o db via configuração global

    # Registrar as blueprints
    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
