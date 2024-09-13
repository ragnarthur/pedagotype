from app import create_app

# Cria a aplicação Flask
app = create_app()

# A função app.run() só deve ser usada no ambiente de desenvolvimento
if __name__ == '__main__':
    app.run(debug=False)  # Utilize debug=True apenas para desenvolvimento local
