# 📝 Gerenciador de Tarefas (Python + SQLite)

Aplicação simples de terminal para gerenciar tarefas, usando Python 3 e banco de dados SQLite.

## 📚 Funcionalidades

- ✅ Adicionar novas tarefas
- 📋 Listar tarefas existentes
- ✏️ Editar título e descrição
- ✔️ Marcar tarefa como concluída
- ❌ Excluir tarefa

## 🗂 Estrutura do Projeto

gerenciador_tarefas/
├── database/
│ └── tarefas.db # Banco de dados SQLite
│ └── init_db.py # Script para criar o banco
├── main.py # Menu interativo via terminal
├── tarefa.py # Funções de CRUD
└── README.md

## 🚀 Como executar

1. Clone o repositório:
git clone https://github.com/seu-usuario/gerenciador-tarefas.git
cd gerenciador-tarefas
Crie o banco de dados (uma vez só):

py database/init_db.py
Rode o sistema:

py main.py
🐍 Requisitos
Python 3.10+ (vem com suporte ao SQLite por padrão)

Feito por [Vinicius Vieira] 🤘
