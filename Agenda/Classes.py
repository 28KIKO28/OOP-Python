import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    materia TEXT NOT NULL,
    estado 'Pendente',
    data_entrega DATE NOT NULL,
)
""")

conexao.commit()

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.alunos = []
        self.professores = []

    def adicionar_tarefa(self, tarefa, data_entrega, disciplina):
        cursor.execute("""
        INSERT INTO tarefas (titulo, materia, dataentrega)
        VALUES (?, ?, ?)
        """, (tarefa, disciplina, data_entrega))

        conexao.commit()

    def add_teacher(self, professor):
        if professor not in self.professores:
           self.professores.append(professor)

        if self not in professor.turmas:
            professor.turmas.append(self)


class Professor:
    def __init__(self, nome, disciplina, user, password, turmas=None):
        self.nome = nome
        self.disciplina = disciplina
        self.user = user
        self.password = password
        self.turmas = turmas if turmas else []

    def add_task(self, turma, tarefa, data_entrega):

        if turma not in self.turmas:
            print(f"⚠️ {self.nome} não leciona a turma {turma.nome_turma}")
            return

        turma.adicionar_tarefa(tarefa, data_entrega, self.disciplina)

        for aluno in turma.alunos:
            aluno.atualizar_json(tarefa, data_entrega, self.disciplina)


class Aluno:
    def __init__(self, nome, user, password, turma):
        self.nome = nome
        self.user = user
        self.password = password
        self.turma = turma
        self.tarefas = []

        turma.alunos.append(self)

    def atualizar_json(self, tarefa, data_entrega, disciplina):
        tarefa_str = f"Tarefa: {tarefa}; Disciplina: {disciplina}; Data: {data_entrega}; Estado: Pendente\n"
        self.tarefas.append(tarefa_str)

        nome_ficheiro = f"{self.turma.nome_turma}_tarefas.json"

        with open(nome_ficheiro, "a", encoding="utf-8") as file:
            file.write(tarefa_str)
