
# PedagoType

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-2.0-green.svg)](https://flask.palletsprojects.com/)

PedagoType é uma aplicação web projetada para auxiliar no aprendizado de digitação com foco pedagógico. Esta aplicação oferece uma experiência interativa onde os usuários podem aprimorar suas habilidades de digitação enquanto interagem com conteúdos educativos.

## Índice
- Recursos
- Novas Funcionalidades e Melhorias
- Instalação e Configuração
- Estrutura do Projeto
- Tecnologias Utilizadas
- Contribuição
- Licença

## Recursos
- Prática de digitação com diferentes níveis de dificuldade.
- Rastreamento de progresso com pontuação e textos completados.
- Sistema de autenticação seguro com armazenamento de progresso.
- Interface amigável e responsiva para dispositivos móveis.
- Integração com MongoDB para persistência de dados.

## Novas Funcionalidades e Melhorias
- Implementação de um modal de pontuação aprimorado para melhor feedback do usuário ao concluir um texto.
- Correção do foco do modal para garantir que ele apareça centralizado e acima de outros elementos da página.
- Melhoria na lógica de pontuação para fornecer um feedback mais preciso e justo.
- Ajustes de layout e animações para uma experiência de usuário mais envolvente.
- Implementação de navegação automática para o próximo texto após a conclusão e confirmação pelo usuário.
- Conexão e configuração com o MongoDB na Vercel para persistência de dados em produção.
- Atualização do processo de autenticação e gerenciamento de sessões para maior segurança e confiabilidade.
- Ajuste da configuração de deploy na Vercel para suportar a nova arquitetura da aplicação.
- Documentação detalhada do processo de deploy, incluindo integração com domínios personalizados.

## Instalação e Configuração
### Requisitos Pré-instalados
- Python 3.11
- MongoDB
- Git

### Passo a Passo
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ragnarthur/pedagotype.git
   cd pedagotype
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Para Linux/Mac
   .\.venv\Scripts\activate  # Para Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes configurações:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   MONGO_URI=mongodb://localhost:27017/pedagotype_db
   SECRET_KEY=sua_chave_secreta
   ```

5. **Inicie o servidor Flask:**
   ```bash
   flask run
   ```
   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Estrutura do Projeto
```bash
pedagotype/
│
├── app/
│   ├── static/          # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/       # Templates HTML
│   ├── __init__.py      # Inicialização da aplicação Flask
│   ├── models.py        # Definição dos modelos de dados
│   ├── routes.py        # Definição das rotas da aplicação
│   └── forms.py         # Definição dos formulários
│
├── .env                 # Arquivo de variáveis de ambiente
├── .gitignore           # Arquivos e pastas ignorados no controle de versão
├── README.md            # Documentação do projeto
├── requirements.txt     # Dependências do projeto
├── run.py               # Ponto de entrada da aplicação Flask
└── .venv/               # Ambiente virtual (não incluído no repositório)
```

## Tecnologias Utilizadas
- **Python 3.11** - Linguagem de programação utilizada.
- **Flask** - Framework web para desenvolvimento da aplicação.
- **MongoDB** - Banco de dados NoSQL para armazenamento de dados.
- **HTML/CSS/JavaScript** - Para a construção do front-end.
- **Bootstrap** - Framework CSS para design responsivo.

## Contribuição
Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:
1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

# PedagoType - Complete Documentation (English)

## Introduction
PedagoType is a web application designed to assist in learning typing with a pedagogical approach. It offers an interactive experience where users can improve their typing skills while engaging with educational content.

## Table of Contents
- Features
- New Features and Improvements
- Installation and Configuration
- Project Structure
- Technologies Used
- Contribution
- License

## Features
- Typing practice with different levels of difficulty.
- Progress tracking with scores and completed texts.
- Secure user authentication with progress storage.
- User-friendly and responsive interface for mobile devices.
- Integration with MongoDB for data persistence.

## New Features and Improvements
- Implementation of an enhanced scoring modal to provide better user feedback upon text completion.
- Fixed modal focus to ensure it appears centered and above other page elements.
- Improved scoring logic to provide more accurate and fair feedback.
- Layout and animation adjustments for a more engaging user experience.
- Automatic navigation to the next text upon completion and user confirmation.
- Connection and configuration with MongoDB on Vercel for data persistence in production.
- Updated authentication and session management for enhanced security and reliability.
- Adjusted deployment configuration on Vercel to support the new application architecture.
- Detailed documentation of the deployment process, including integration with custom domains.

## Installation and Configuration
### Prerequisites
- Python 3.11
- MongoDB
- Git

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/ragnarthur/pedagotype.git
   cd pedagotype
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .\.venv\Scripts\activate  # For Windows
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add the following settings:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   MONGO_URI=mongodb://localhost:27017/pedagotype_db
   SECRET_KEY=your_secret_key
   ```

5. **Start the Flask server:**
   ```bash
   flask run
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Project Structure
```bash
pedagotype/
│
├── app/
│   ├── static/          # Static files (CSS, JS, images)
│   ├── templates/       # HTML templates
│   ├── __init__.py      # Flask application initialization
│   ├── models.py        # Data models definition
│   ├── routes.py        # Application routes definition
│   └── forms.py         # Forms definition
│
├── .env                 # Environment variables file
├── .gitignore           # Files and folders ignored in version control
├── README.md            # Project documentation
├── requirements.txt     # Project dependencies
├── run.py               # Flask application entry point
└── .venv/               # Virtual environment (not included in the repository)
```

## Technologies Used
- **Python 3.11** - Programming language used.
- **Flask** - Web framework for application development.
- **MongoDB** - NoSQL database for data storage.
- **HTML/CSS/JavaScript** - For building the front-end.
- **Bootstrap** - CSS framework for responsive design.

## Contribution
Contributions are welcome! To contribute, follow these steps:
1. Fork the project.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.