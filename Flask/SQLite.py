import sqlite3

def conectar_login():
    return sqlite3.connect("users.db")


def login_tabela():
    con = conectar_login()
    cursor = con.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            nickname TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('aluno','professor','dt','admin')),
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profs_turmas (
            user_id INTEGER USERS(id),
            turmas 
        )
    """)

    con.commit()
    con.close()


def criar_conta(login, nickname, password, role):

    con = conectar_login()
    cursor = con.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO users (login, nickname, password, role, turma_id)
            VALUES (?, ?, ?, ?, ?)
            """,
            (login, nickname, password, role, turma_id)
        )
        user_id = cursor.lastrowid

        # se for professor ou dt e foram fornecidas turma+disciplina, insere ligação
        if role in ('professor', 'dt') and turma_id is not None and disciplina_id is not None:
            cursor.execute(
                """
                INSERT OR IGNORE INTO profs_turmas (user_id, turma_id, disciplina_id, nivel_acesso)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, turma_id, disciplina_id, nivel_acesso)
            )

        con.commit()
        return user_id
    except sqlite3.IntegrityError as e:
        con.rollback()
        raise
    finally:
        con.close()


# --- Funções relacionadas com tarefas (corrigidas) ---

def conectar_tarefas():
    return sqlite3.connect("tasks.db")


def criar_tabela_tarefas():
    con = conectar_tarefas()
    cursor = con.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        subjects TEXT NOT NULL,
        status TEXT NOT NULL,
        due_date DATE NOT NULL,
        prioritie TEXT NOT NULL,
        teacher TEXT NOT NULL
    )
    """)
    con.commit()
    con.close()


def adicionar_tarefa(title, subject, status, prioritie, teacher, classe):
    con = conectar_tarefas()
    cursor = con.cursor()
    cursor.execute("""
    INSERT INTO tarefas (task, subjects, status, prioritie, teacher, teacher)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (title, subject, status, prioritie, teacher, classe))
    con.commit()
    con.close()


def tarefas_concluir(escolha_index):
    con = conectar_tarefas()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    con.close()
    if 0 <= escolha_index < len(tarefas):
        return tarefas[escolha_index]
    return None


def tarefas_ler():
    con = conectar_tarefas()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    con.close()
    if not tarefas:
        return False
    return tarefas
