
# PedagoType

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-2.0-green.svg)](https://flask.palletsprojects.com/)

PedagoType é um aplicativo web desenvolvido para auxiliar no aprendizado de digitação com foco pedagógico. Ele integra a prática de digitação com conceitos educativos, permitindo que os usuários aprimorem suas habilidades de digitação enquanto se engajam em conteúdos educacionais interativos.

## Índice

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Recursos

- Prática de digitação com textos organizados por níveis de dificuldade.
- Registro de progresso do usuário (pontuação e textos finalizados).
- Integração com banco de dados para salvar e carregar o progresso.
- Interface interativa e responsiva com suporte a dispositivos móveis.
- Modalidades de cadastro e login com autenticação segura.
- Feedback imediato com efeito "shake" em caso de erros na digitação.
- Suporte a múltiplos usuários e persistência dos dados de cada um.

## Instalação

Para clonar o repositório e configurar o projeto localmente, siga as etapas abaixo:

1. Clone o repositório:

   ```bash
   git clone https://github.com/ragnarthur/pedagotype.git
   cd pedagotype
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Para Linux/Mac
   .\.venv\Scripts\activate    # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie o arquivo `.env` com suas variáveis de ambiente:

   ```bash
   touch .env
   ```

   No arquivo `.env`, defina as variáveis necessárias:

   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   MONGO_URI=mongodb://localhost:27017/pedagotype_db
   SECRET_KEY=sua_chave_secreta
   ```

5. Inicie o servidor Flask:

   ```bash
   flask run
   ```

   O aplicativo estará disponível em `http://127.0.0.1:5000`.

## Configuração

### Banco de Dados

O **PedagoType** utiliza o **MongoDB** como banco de dados principal. Certifique-se de ter o MongoDB instalado e rodando em sua máquina local. A URI de conexão pode ser configurada no arquivo `.env`.

### Dependências

A aplicação utiliza as seguintes dependências:

- Flask
- Flask-PyMongo
- Flask-Login
- Jinja2
- JavaScript e CSS personalizados

Você pode encontrar todas as dependências listadas no arquivo `requirements.txt`.

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

- **Python** (versão 3.11) - Linguagem de programação principal.
- **Flask** - Framework web leve utilizado para criar a aplicação.
- **MongoDB** - Banco de dados NoSQL utilizado para persistência dos dados.
- **Jinja2** - Engine de templates para renderização das páginas HTML.
- **HTML/CSS/JavaScript** - Estrutura e estilização do front-end.
- **Bootstrap** - Framework CSS para layout responsivo.

## Contribuição

Contribuições são sempre bem-vindas! Se você deseja contribuir com melhorias ou novas funcionalidades, siga os seguintes passos:

1. Faça um fork do projeto.
2. Crie uma branch com sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie para o GitHub (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
