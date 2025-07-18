import sqlite3
import os

CAMINHO_DB = os.path.join('database', 'tarefas.db')

def conectar():
    return sqlite3.connect(CAMINHO_DB)

def adicionar_tarefa(titulo, descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)", (titulo, descricao))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, descricao, status FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def atualizar_tarefa(id, novo_titulo, nova_descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?", (novo_titulo, nova_descricao, id))
    conn.commit()
    conn.close()

def concluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def excluir_tarefa(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
