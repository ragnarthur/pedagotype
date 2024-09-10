from app import create_app

# Cria a aplicação Flask e o banco de dados
app, db = create_app()

if __name__ == '__main__':
    # Iniciar o servidor Flask
    app.run(debug=True, host='0.0.0.0', port=5000)
