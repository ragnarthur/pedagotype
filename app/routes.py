from flask import Blueprint, render_template, request, jsonify
from .texts import get_ordered_text

main = Blueprint('main', __name__)

# Rota para a página inicial
@main.route('/')
def index():
    return render_template('base.html')

# Rota para obter o próximo texto via AJAX (usada no script.js)
@main.route('/get_text')
def get_text():
    index = int(request.args.get('index', 0))  # Pega o índice do texto
    text = get_ordered_text(index)  # Obtém o texto com base no índice
    return jsonify({'text': text})  # Retorna o texto em formato JSON

# Rota para a página "Sobre"
@main.route('/sobre')
def about():
    return render_template('sobre.html')

# Rota para a página de Treinamento
@main.route('/treinamento')
def treinamento():
    return render_template('treinamento.html')

# Rota para salvar a pontuação do usuário
@main.route('/save_score', methods=['POST'])
def save_score():
    score = request.json.get('score')
    index = request.json.get('index')
    # Aqui você pode implementar a lógica para salvar a pontuação no banco de dados
    # Exemplo: db.scores.insert_one({'score': score, 'exercise_id': index})
    return jsonify({'message': 'Pontuação salva com sucesso!'})


@main.route('/contato')
def contato():
    return render_template('contato.html')
