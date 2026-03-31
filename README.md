# API Flask com Autenticação e Frontend

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma API REST utilizando Flask, integrada a um frontend simples em HTML, CSS e JavaScript.

A aplicação permite:

- Cadastro de usuários  
- Login com autenticação  
- Geração de token de acesso  
- Inserção de dados vinculados ao usuário  
- Listagem dos dados do usuário autenticado  

O objetivo do projeto é aplicar conceitos de:

- Desenvolvimento de APIs  
- Separação de camadas (controller, service e database)  
- Autenticação via token  
- Integração entre backend e frontend  

---

## 🧱 Estrutura do Projeto

flask-api/
│── app.py
│── database.py
│── service.py
│── auth.py
│── requirements.txt
│── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

---

## ⚙️ Tecnologias Utilizadas

- Python 3  
- Flask  
- SQLite  
- HTML5  
- CSS3  
- JavaScript  

---

## 🔐 Funcionalidades

### 👤 Cadastro de Usuário
Permite cadastrar um novo usuário com:
- Nome  
- Email  
- Senha (armazenada com hash)  

### 🔑 Login
Realiza autenticação do usuário e retorna:
- Token de acesso  
- Dados do usuário  

### 📊 Inserção de Dados
Usuário autenticado pode cadastrar dados próprios.

### 📋 Listagem de Dados
Usuário autenticado pode visualizar seus dados cadastrados.

---

## 🔒 Autenticação

A autenticação é feita via token no header da requisição:

Authorization: Bearer SEU_TOKEN_AQUI

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

git clone https://github.com/seu-usuario/seu-repositorio.git  
cd seu-repositorio  

### 2. Instalar dependências

pip install -r requirements.txt  

### 3. Executar a aplicação

python app.py  

### 4. Acessar no navegador

http://localhost:5000  

---

## 🧪 Fluxo de Testes

1. Cadastrar um usuário  
2. Realizar login  
3. Inserir um novo dado  
4. Listar os dados cadastrados  

---

## 🧠 Arquitetura do Projeto

O projeto segue separação de responsabilidades:

- app.py → Rotas e controle da aplicação  
- service.py → Regras de negócio  
- database.py → Acesso ao banco de dados  
- auth.py → Controle de autenticação  
- Frontend (HTML/CSS/JS) → Interface do usuário  

---

## 👨‍💻 Participantes

- João Inácio C Moraes  
  RA: 1135445  

- Luis Zanin  
  RA: 1136493  

---

## 📎 Observações

- O banco de dados é criado automaticamente ao iniciar a aplicação  
- Os dados são persistidos em SQLite  
- O sistema foi desenvolvido com foco em simplicidade e aprendizado  

---

## 📌 Conclusão

O projeto demonstra a implementação completa de uma aplicação web simples com autenticação, integração frontend/backend e boas práticas de organização de código.
