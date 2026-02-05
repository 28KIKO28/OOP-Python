from flask import Flask, render_template,request,redirect
from os import O_APPEND
import calendar
import datetime

app = Flask(__name__)

lista_turmas = [
    (10, 1, 20, "Joaquim", ["Filipe", "Ana", "Carla", "Joana", "Mariana", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Lucas", "Samantha", "Tiago", "Camila", "Pedro", "Juliana", "Bruno", "Larissa", "Diego", "Amanda", "Felipe"]), 
    (10, 2, 20, "Pedro", ["Marcos", "Paula", "Juliana", "Camila", "Bruno", "Larissa", "Diego", "Amanda", "Felipe", "Renata", "César", "Vivian", "Rodrigo", "Patrícia", "Eduardo", "Simone", "Fábio", "Aline", "Guilherme", "Isabela"]), 
    (10, 3, 20, "Benedito", ["Sofia", "Matheus", "Isabela", "Gabriel", "Yasmin", "Thiago", "Lara", "Vitor", "Nicole", "Enzo", "Luna", "Davi", "Helena", "Samuel", "Clara", "Rafael", "Marina", "Cecília", "Guilherme", "Alice"]),
    (10, 4, 20, "Mariana", ["Eduardo" , "Bianca" , "Felipe" , "Larissa" , "Rafael" , "Amanda" , "Gustavo" , "Isadora" , "Bruna" , "Caio" , "Letícia" , "Vinícius", "Mariana", "Leonardo", "Sabrina", "Daniel", "Camila", "Bruno", "Natália", "Lucas"]),
    (10, 5, 20, "Lucas", ["Renan", "Sabrina", "Thiago", "Vanessa", "Wesley", "Ximena", "Yago", "Zara", "Aline", "Brenda", "Caetano", "Daniel", "Emanuel", "Fabiana", "Geraldo", "Heloísa", "Igor", "Jéssica", "Kléber", "Larissa"]),
    (10, 6, 20, "Fernanda", ["Mário", "Natasha", "Olívia", "Júlia", "Kauã", "Lívia", "Murilo", "Nina", "Otávio", "Pietro", "Quirino", "Rosa", "Sandro", "Tatiana", "Ubirajara", "Valentina", "William", "Xandra", "Yasmin", "Zeca"]),
    (10, 7, 20, "Ricardo", ["Vanessa", "Wesley", "Ximena", "Yago", "Zara", "Aline", "Brenda", "Caetano", "Daniel", "Emanuel", "Fabiana", "Geraldo", "Heloísa", "Igor", "Jéssica", "Kléber", "Larissa", "Mário", "Natasha", "Olívia"]),
    (10, 8, 20, "Sílvia", ["Júlia", "Kauã", "Lívia", "Murilo", "Nina", "Otávio", "Pietro", "Quirino", "Rosa", "Sandro", "Tatiana", "Ubirajara", "Valentina", "William", "Xandra", "Yasmin", "Zeca", "Alice", "Bruno", "Catarina"]),
    (10, 9, 20, "Filipe", ["Tatiana", "Ursula", "Vitor", "Wagner", "Xuxa", "Yuri", "Zélia", "Amanda", "Bruno", "Camila", "Diego", "Eduarda", "Fábio", "Gabriela", "Hugo", "Isadora", "João", "Kátia", "Leonardo", "Marina", "Nicolas"])
]

tarefas = []

@app.route("/")
def turmas ():
    return render_template ("turmas.html", lista_turmas=lista_turmas)

@app.route("/class/<int:indice>")
def alunos (indice):
    turma = lista_turmas[indice]
    alunos = sorted(turma[4])
    return render_template ("alunos.html", turma=turma, alunos=alunos)

@app.route("/add", methods=["post"])
def adicionar():
    nova_tarefa = (
        request.form["tarefa"],request.form["disciplina"],request.form["prioridade"],request.form["data"],"Pendente")
    tarefas.append(nova_tarefa)
    return redirect("/tasks")

@app.route("/tasks")
def listar_tarefas():
    return render_template("listatarefas.html", tarefas=tarefas)

@app.route("/addtask")
def nova_tarefa_form():
    return render_template("tarefas.html")

app.run(debug=True, host='0.0.0.0')