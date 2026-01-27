class Turma:
    def __init__(self, nome_turma, alunos, professores):
        self.nome_turma = nome_turma
        self.alunos = alunos
        self.professores = professores

    def adicionar_tarefa(self, tarefa, data_entrega, disciplina):
        with open(self.nome_turma + ".json", "a", encoding="utf-8") as file:
            file.write(f"Tarefa: {tarefa}; Disciplina: {disciplina}; Data: {data_entrega}; Estado: Pendente\n")

    def add_teacher(self, professor):
        if professor not in self.professores:
           self.professores.append(professor)
           print("Professor adicionado")
        if self.nome_turma not in professor.turmas:
            professor.turmas.append(self)
            print("Professor adicionado")
        if professor in self.professores:
            print("O professor já está associado a esta turma.")
        
    def turma_alunos(self):
        for aluno in self.alunos:
            aluno.nome_turma = self.nome_turma

    def apagar_tarefas(self):
        with open(self.nome_turma + ".json", "w", encoding="utf-8") as file:
            file.write("")

class Professor:
    def __init__(self, nome, disciplina, user, password, turmas=None):
        self.nome = nome
        self.disciplina = disciplina
        self.user = user
        self.password = password
        self.turmas = turmas if turmas else []

    def add_task(self, turma, tarefa, data_entrega):
        if self not in turma.professores:
            print(f"⚠️ {self.nome} não leciona a turma {turma.nome_turma}")
        else:
            print(f"✅ {self.nome} leciona a turma {turma.nome_turma}")
            turma.adicionar_tarefa(tarefa, data_entrega, self.disciplina)
            print(f"Tarefa: {tarefa} adicionada para a turma {turma.nome_turma}")

class Aluno:
    def __init__(self, nome, user, password):
        self.nome = nome
        self.user = user
        self.password = password
        self.nome_turma = []

    def printar_tarefas(self):
        with open(self.nome_turma + ".json", "r", encoding="utf-8") as file:
            tarefas = file.readlines()
            if not tarefas:
                print("Nenhuma tarefa atribuída.")
            else:
                for tarefa in tarefas:
                    print(tarefa.strip())

filipee = Professor("Filipe", "Matemática", "filipe123", "senha123")
aluno1 = Aluno("Ana", "ana123", "senha123")
aluno2 = Aluno("Bruno", "bruno123", "senha123")
turma1 = Turma("10º1", [aluno1, aluno2], [filipee])
turma1.turma_alunos()
aluno1.printar_tarefas()