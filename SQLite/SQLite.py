import sqlite3

def conectar_login():
    return sqlite3.connect("users.db")
def login_tabela():
    con = conectar_login
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            nickname TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT CHECK(role in ('student','teacher','admin','dt')) TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()
def criar_conta():
    con = conectar_login
    cursor = con.cursor
    cursor.cursor()

def conectar_tarefas():
    return sqlite3.connect("tasks.db")

def criar_tabela_tarefas():
    con = conectar_tarefas()
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        subject TEXT NOT NULL,
        status TEXT NOT NULL,
        due_date DATE NOT NULL,
        prioritie TEXT NOT NULL,
        teacher TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()

def adicionar_tarefa(tittle, subject, status, prioritie, teacher):
    con = conectar_tarefas()
    con.execute("""INSERT INTO tarefas (task, subject, status, prioritie, teacher)
    VALUES (?, ?, ?, ?, ?)
    """, (tittle, subject, status, prioritie, teacher))
    con.commit()
    con.close()

def tarefas_concluir():
        con = conectar_tarefas
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
def tarefas_ler():
    con = conectar_tarefas
    cursor = con.cursor()
    con.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    if not tarefas:
        tarefas = False
        return tarefas
    else:
        return tarefas

""" 
while True:
    if escolha == 'Apagar':
        print()
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        for i, tarefa in enumerate(tarefas, start=0):
            print(f"{i+1}ª Tarefa - Titulo: {tarefa[1]}, Matéria: {tarefa[2]}, Estado: {tarefa[3]}")
            tarefa_apagar = int(input("Digite o número da tarefa que deseja apagar: ")) - 1
        if 0 <= tarefa_apagar < len(tarefas):
            tarefa_id = tarefas[tarefa_apagar][0]
            cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
            conexao.commit()
            print("Tarefa apagada.\n")
        else:
            print("Essa tarefa não existe.\n")
    elif escolha == 'Concluir':
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        for i, tarefa in enumerate(tarefas, start=0):
            print(f"{i+1}ª Tarefa - Titulo: {tarefa[1]}, Matéria: {tarefa[2]}, Estado: {tarefa[3]}")
        tarefa_concluir = int(input("Digite o número da tarefa que deseja concluir: ")) - 1
        if 0 <= tarefa_concluir < len(tarefas):
            tarefa_id = tarefas[tarefa_concluir][0]
            cursor.execute("UPDATE tarefas SET status = 'Concluída' WHERE id = ?", (tarefa_id,))
            conexao.commit()
            print("Tarefa concluída.\n")
        else:
            print("Essa tarefa não existe.\n")
"""