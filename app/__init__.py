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

    # Importa as rotas apenas após criar o app
    from .routes import main
    app.register_blueprint(main)

    return app, db
