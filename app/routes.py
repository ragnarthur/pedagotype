from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/start_typing', methods=['GET', 'POST'])
def start_typing():
    if request.method == 'POST':
        # Lógica para iniciar o treino de digitação
        pass
    return render_template('start_typing.html')

@main.route('/about')
def about():
    return render_template('about.html')
