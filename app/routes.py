from flask import Blueprint, render_template, jsonify, request, session, current_app
from .texts import get_next_uncompleted_text
from .auth import login_required
from pymongo import MongoClient
import os

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html')

# Rota de Treinamento (treinamento.html)
@main.route('/treinamento')
@login_required
def treinamento():
    db = current_app.config['db']
    user = session.get('user')
    
    # Verifica se o usuário tem um last_text_id salvo no banco de dados
    user_data = db.users.find_one({'email': user})
    last_text_id = user_data.get('last_text_id', 0)  # Se não houver, começa do texto 0

    return render_template('treinamento.html', last_text_id=last_text_id)


# Rota para obter o próximo texto (pode ser protegida se necessário)
@main.route('/get_text')
@login_required
def get_text():
    db = current_app.config['db']
    user = session.get('user')

    # Recupera o usuário e os textos já completados
    user_data = db.users.find_one({'email': user})
    completed_text_ids = user_data.get('completed_text_ids', [])

    # Obtém o próximo texto que o usuário ainda não completou
    next_text_data = get_next_uncompleted_text(completed_text_ids)
    
    if next_text_data:
        return jsonify(text=next_text_data['text'], id=next_text_data['id'])  # Retorna texto e ID
    else:
        return jsonify(error="Todos os textos foram completados!"), 200
    
# Rota para a página "Sobre" (apenas para usuários logados)
@main.route('/sobre')
@login_required
def about():
    return render_template('sobre.html')

# Rota para a página "Contato" (apenas para usuários logados)
@main.route('/contato')
@login_required
def contato():
    return render_template('contato.html')

# Rota para salvar a pontuação do usuário e registrar o texto completado
@main.route('/save_score', methods=['POST'])
@login_required
def save_score():
    db = current_app.config['db']
    
    score = request.json.get('score')
    text_id = request.json.get('text_id')
    
    # Obter o usuário logado
    logged_in_user = session.get('user')
    
    if logged_in_user and score is not None and text_id is not None:
        # Recuperar a pontuação existente do usuário
        user_data = db.users.find_one({'email': logged_in_user}, {'score': 1})
        current_score = user_data.get('score', 0)

        # Somar a nova pontuação à existente
        updated_score = current_score + score

        # Atualizar o usuário no banco de dados com a nova pontuação e o texto completado
        db.users.update_one(
            {'email': logged_in_user},
            {
                '$set': {'score': updated_score, 'last_text_id': text_id},
                '$addToSet': {'completed_text_ids': text_id}  # Adiciona o texto ao conjunto de textos completados
            }
        )
        return jsonify({'message': 'Pontuação e texto salvos com sucesso!'}), 200
    else:
        return jsonify({'error': 'Dados inválidos'}), 400
    
@main.route('/progresso')
@login_required
def progresso():
    db = current_app.config['db']
    users = list(db.users.find({}, {'_id': 0, 'name': 1, 'score': 1}))  # Exclui o _id do MongoDB

    logged_in_user = session.get('user')
    user_score = None

    for user in users:
        if user['name'] == logged_in_user:
            user_score = user['score']

    return render_template('progresso.html', users=users, user_score=user_score, logged_in_user=logged_in_user)


@main.route('/get_last_text_id')
@login_required
def get_last_text_id():
    db = current_app.config['db']
    
    # Obter o usuário logado
    logged_in_user = session.get('user')
    
    if logged_in_user:
        # Recupera o last_text_id do banco de dados
        user_data = db.users.find_one({'email': logged_in_user}, {'_id': 0, 'last_text_id': 1})
        if user_data and 'last_text_id' in user_data:
            return jsonify({'last_text_id': user_data['last_text_id']}), 200
        else:
            return jsonify({'last_text_id': 0}), 200  # Se não houver last_text_id, retorna 0
    else:
        return jsonify({'error': 'Usuário não autenticado'}), 401


@main.route('/test-mongo')
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