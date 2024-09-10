from flask import Blueprint, jsonify, request
from . import create_app

app, db = create_app()

api = Blueprint('api', __name__)

# Exemplo de rota GET para listar usuários
@api.route('/api/users', methods=['GET'])
def get_users():
    users = db.users.find()
    output = []
    for user in users:
        user_data = {'name': user['name'], 'score': user['score']}
        output.append(user_data)
    return jsonify({'users': output})

# Exemplo de rota POST para adicionar um novo usuário
@api.route('/api/users', methods=['POST'])
def add_user():
    new_user = {
        'name': request.json['name'],
        'score': request.json.get('score', 0)
    }
    db.users.insert_one(new_user)
    return jsonify({'message': 'User added successfully!'}), 201

# Exemplo de rota PUT para atualizar o score de um usuário
@api.route('/api/users/<name>', methods=['PUT'])
def update_user(name):
    new_score = request.json['score']
    db.users.update_one({'name': name}, {'$set': {'score': new_score}})
    return jsonify({'message': f'Score for {name} updated successfully!'})

# Exemplo de rota DELETE para remover um usuário
@api.route('/api/users/<name>', methods=['DELETE'])
def delete_user(name):
    db.users.delete_one({'name': name})
    return jsonify({'message': f'User {name} deleted successfully!'})
