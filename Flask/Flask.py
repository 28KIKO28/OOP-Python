from flask import Flask
from flask import render_template

app = Flask(__name__)

turma1 = ["Filipe", "Ana", "Carla", "Joana", "Mariana", "Rafael", "Beatriz", "Gustavo", "Fernanda", "Lucas", "Samantha", "Tiago", "Camila", "Pedro", "Juliana", "Bruno", "Larissa", "Diego", "Amanda", "Felipe"]
turma2 = ["Marcos", "Paula", "Juliana", "Camila", "Bruno", "Larissa", "Diego", "Amanda", "Felipe", "Renata", "César", "Vivian", "Rodrigo", "Patrícia", "Eduardo", "Simone", "Fábio", "Aline", "Guilherme", "Isabela"]
turma3 = ["Sofia", "Matheus", "Isabela", "Gabriel", "Yasmin", "Thiago", "Lara", "Vitor", "Nicole", "Enzo", "Luna", "Davi", "Helena", "Samuel", "Clara", "Rafael", "Marina", "Cecília", "Guilherme", "Alice"]
turma4 = ["Eduardo" , "Bianca" , "Felipe" , "Larissa" , "Rafael" , "Amanda" , "Gustavo" , "Isadora" , "Bruna" , "Caio" , "Letícia" , "Vinícius", "Mariana", "Leonardo", "Sabrina", "Daniel", "Camila", "Bruno", "Natália", "Lucas"]
turma5 = ["Renan", "Sabrina", "Thiago", "Vanessa", "Wesley", "Ximena", "Yago", "Zara", "Aline", "Brenda", "Caetano", "Daniel", "Emanuel", "Fabiana", "Geraldo", "Heloísa", "Igor", "Jéssica", "Kléber", "Larissa"]
turma6 = ["Mário", "Natasha", "Olívia", "Júlia", "Kauã", "Lívia", "Murilo", "Nina", "Otávio", "Pietro", "Quirino", "Rosa", "Sandro", "Tatiana", "Ubirajara", "Valentina", "William", "Xandra", "Yasmin", "Zeca"]
turma7 = ["Vanessa", "Wesley", "Ximena", "Yago", "Zara", "Aline", "Brenda", "Caetano", "Daniel", "Emanuel", "Fabiana", "Geraldo", "Heloísa", "Igor", "Jéssica", "Kléber", "Larissa", "Mário", "Natasha", "Olívia"]
turma8 = ["Júlia", "Kauã", "Lívia", "Murilo", "Nina", "Otávio", "Pietro", "Quirino", "Rosa", "Sandro", "Tatiana", "Ubirajara", "Valentina", "William", "Xandra", "Yasmin", "Zeca", "Alice", "Bruno", "Catarina"]
turma9 = ["Ursula", "Vitor", "Wagner", "Xuxa", "Yuri", "Zélia", "Amanda", "Bruno", "Camila", "Diego", "Eduarda", "Fábio", "Gabriela", "Hugo", "Isadora", "João", "Kátia", "Leonardo", "Marina", "Nicolas"]

lista_turmas = [
    (10, 1, 20, "Joaquim", turma1), 
    (10, 2, 20, "Pedro", turma2), 
    (10, 3, 20, "Benedito", turma3),
    (10, 4, 20, "Mariana", turma4),
    (10, 5, 20, "Lucas", turma5),
    (10, 6, 20, "Fernanda", turma6),
    (10, 7, 20, "Ricardo", turma7),
    (10, 8, 20, "Sílvia", turma8),
    (10, 9, 20, "Tatiana", turma9)
]
@app.route("/")
def turmas ():
    return render_template ("turmas.html", lista_turmas=lista_turmas)

@app.route("/alunos/<int:indice>")
def alunos (indice):
    turma = lista_turmas[indice]
    alunos = sorted(turma[4])
    return render_template ("alunos.html", turma=turma, alunos=alunos)
    
app.run(debug=True, host='0.0.0.0')
