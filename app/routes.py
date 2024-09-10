from flask import Blueprint, render_template, jsonify, request
from .texts import get_ordered_text
from .auth import login_required

main = Blueprint('main', __name__)

# Rota para a página inicial (acessível a todos)
@main.route('/')
def index():
    return render_template('base.html')

# Rota para o treinamento (apenas para usuários logados)
@main.route('/treinamento')
@login_required
def treinamento():
    return render_template('treinamento.html')

# Rota para obter o próximo texto (pode ser protegida se necessário)
@main.route('/get_text')
@login_required
def get_text():
    index = int(request.args.get('index', 0))
    text = get_ordered_text(index)
    return jsonify({'text': text})

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

# Rota para salvar a pontuação do usuário (apenas para usuários logados)
@main.route('/save_score', methods=['POST'])
@login_required
def save_score():
    score = request.json.get('score')
    index = request.json.get('index')
    # Aqui você pode implementar a lógica para salvar a pontuação no banco de dados
    return jsonify({'message': 'Pontuação salva com sucesso!'})
