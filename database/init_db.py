import sqlite3
import os

caminho_db = os.path.join(os.path.dirname(__file__), 'tarefas.db')

def criar_tabela():
    conexao = sqlite3.connect(caminho_db)
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'pendente'
        );
    """)
    
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados e tabela criados com sucesso!")
