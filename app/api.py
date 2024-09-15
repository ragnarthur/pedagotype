from flask import Blueprint, jsonify, request, current_app
from pymongo import MongoClient
import os

api = Blueprint('api', __name__)

# Rota GET para listar usuários
@api.route('/api/users', methods=['GET'])
def get_users():
    db = current_app.config['db']
    users = db.users.find()
    output = []
    for user in users:
        user_data = {'name': user['name'], 'score': user['score']}
        output.append(user_data)
    return jsonify({'users': output})

# Rota POST para adicionar um novo usuário
@api.route('/api/users', methods=['POST'])
def create_user():
    db = current_app.config['db']
    new_user = {
        'name': request.json['name'],
        'score': request.json.get('score', 0)
    }
    db.users.insert_one(new_user)
    return jsonify({'message': 'User added successfully!'}), 201

# Rota PUT para atualizar o score de um usuário
@api.route('/api/users/<name>', methods=['PUT'])
def update_user_score(name):
    db = current_app.config['db']
    new_score = request.json['score']
    db.users.update_one({'name': name}, {'$set': {'score': new_score}})
    return jsonify({'message': f'Score for {name} updated successfully!'})

# Rota DELETE para remover um usuário
@api.route('/api/users/<name>', methods=['DELETE'])
def delete_user(name):
    db = current_app.config['db']
    db.users.delete_one({'name': name})
    return jsonify({'message': f'User {name} deleted successfully!'})

# Rota para testar a conexão com o MongoDB
@api.route('/test-mongo', methods=['GET'])
def test_mongo():
    try:
        # Obtém a URL do MongoDB das variáveis de ambiente
        mongo_url = os.getenv('MONGO_URL')
        client = MongoClient(mongo_url)
        # Testa a conexão ao banco de dados
        client.server_info()  # Isso irá falhar se não puder se conectar
        return "Conexão com MongoDB estabelecida com sucesso!", 200
    except Exception as e:
        return f"Erro ao conectar ao MongoDB: {str(e)}", 500
