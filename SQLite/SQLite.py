import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = sqlite3.Cursor(conexao)

cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    materia TEXT NOT NULL,
    status TEXT NOT NULL
)
""")


def adicionar_tarefa(tittle, subject, status):
    cursor.execute("""INSERT INTO tarefas (titulo, materia, status)
    VALUES (?, ?, ?)
    """, (tittle, subject, status))
    conexao.commit()

cursor.execute("SELECT * FROM tarefas")
tarefas = cursor.fetchall()
while True:
    escolha = input("[1] - Adicionar tarefa\n[2] - Mostrar tarefas\n[3] - Apagar tarefas\n[4] - Concuir uma tarefa\n[5] - Sair\nEscolha uma opção: ")
    if escolha == '1':
        print()
        titulo = input("Título da tarefa: ")
        materia = input("Matéria: ")
        status = "Pendente"
        adicionar_tarefa(titulo, materia, status)
        print("Tarefa adicionada.\n")
    elif escolha == '2':
        print()
        cursor.execute("SELECT * FROM tarefas")
        tarefas = cursor.fetchall()
        if not tarefas:
            print("Não há tarefas.\n")
        else:
            print("+----+--------------------------------+----------------------+-----------+")
            print("| Nº | Tarefa                         | Matéria              | Estado    |")
            print("+----+--------------------------------+----------------------+-----------+")
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}ª Tarefa | {t[0]:<25} | {t[1]:<20} | {t[2]:<14}")
            print("+----+------------------------------+------------------+-----------+")    

    elif escolha == '3':
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
    elif escolha == '4':
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
    elif escolha == '5':
        print()
        break
    
    else:
        print("Opção inválida. Tente novamente.")
conexao.close()