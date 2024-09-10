from flask import Blueprint, jsonify, request, current_app

api = Blueprint('api', __name__)

# Rota GET para listar usuários
@api.route('/api/users', methods=['POST'])
def add_user():
    db = current_app.config['db']
    
    # Validação de dados
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Invalid data'}), 400

    try:
        new_user = {
            'name': request.json['name'],
            'score': request.json.get('score', 0)
        }
        db.users.insert_one(new_user)
        return jsonify({'message': 'User added successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Rota POST para adicionar um novo usuário
@api.route('/api/users', methods=['POST'])
def add_user():
    db = current_app.config['db']  # Obtém o db do contexto do app
    new_user = {
        'name': request.json['name'],
        'score': request.json.get('score', 0)
    }
    db.users.insert_one(new_user)
    return jsonify({'message': 'User added successfully!'}), 201

# Rota PUT para atualizar o score de um usuário
@api.route('/api/users/<name>', methods=['PUT'])
def update_user(name):
    db = current_app.config['db']  # Obtém o db do contexto do app
    new_score = request.json['score']
    db.users.update_one({'name': name}, {'$set': {'score': new_score}})
    return jsonify({'message': f'Score for {name} updated successfully!'})

# Rota DELETE para remover um usuário
@api.route('/api/users/<name>', methods=['DELETE'])
def delete_user(name):
    db = current_app.config['db']  # Obtém o db do contexto do app
    db.users.delete_one({'name': name})
    return jsonify({'message': f'User {name} deleted successfully!'})
