from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

auth = Blueprint('auth', __name__)

# Decorador para verificar se o usuário está logado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Você precisa estar logado para acessar essa página.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# Rota de Login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = current_app.config['db']
        user = db.users.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            session['user'] = user['email']  # Salva o email na sessão
            flash('Login efetuado com sucesso!', 'success')  # Flash de sucesso
            return redirect(url_for('main.index'))
        else:
            flash('Login inválido. Verifique suas credenciais.', 'danger')  # Flash de erro
            return redirect(url_for('auth.login'))

    return render_template('login.html')

# Rota de Cadastro
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')  # Adiciona o campo 'name' ao formulário

        db = current_app.config['db']
        
        # Verifica se o usuário já existe
        existing_user = db.users.find_one({'email': email})
        
        if existing_user is None:
            # Cria o hash da senha e insere o novo usuário com o nome, email e senha
            hashed_password = generate_password_hash(password, method='scrypt')
            db.users.insert_one({
                'email': email,
                'password': hashed_password,
                'name': name  # Adiciona o nome durante o registro
            })
            flash('Usuário cadastrado com sucesso! Faça login.', 'success')  # Flash de sucesso
            return redirect(url_for('auth.login'))
        
        flash('O email já está cadastrado.', 'danger')  # Flash de erro
    return render_template('register.html')

# Rota de Logout
@auth.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    flash('Você saiu com sucesso.', 'success')  # Flash de sucesso ao sair
    return redirect(url_for('auth.login'))
