import tkinter as tk
import json
import os

def labelcreator():
    label = tk.Label(window, text="Qual a nova tarefa?", font=("Comic Sans", 30))
    tarefainput = tk.Entry(window, width=60, font=("Comic Sans", 20), bd=5)
    label2 = tk.Label(window, text="Qual a matéria?", font=("Comic Sans", 30))
    materiainput = tk.Entry(window, width=60, font=("Comic Sans", 20), bd=5)
    label3 = tk.Label(window, text="Qual o estado?", font=("Comic Sans", 30))
    statusinput = tk.Entry(window, width=60, font=("Comic Sans", 20), bd=5)
    buttom = tk.Button(window, text="Enviar?", font=("Comic Sans", 30), command=lambda: recolhertaf(materiainput,tarefainput,statusinput))

def recolhertaf(materiain,tarefain,statusin):
    global tarefa, materia, status
    tarefa = tarefain.get()
    materia = materiain.get()
    status = statusin.get()
    label.destroy()
    tarefainput.destroy()
    label2.destroy()
    materiainput.destroy()
    label3.destroy()
    statusinput.destroy()
    buttom.destroy()
    print(f"Tarefa : {tarefa}, Matéria: {materia}")
    with open("tarefas.json", "a", encoding="utf-8") as f:
        f.write(f"Tarefa: {tarefa}, Matéria: {materia}, Status: {status}\n")
    labelantefinal = tk.Label(window, text="Nova Tarefa:", font=("Comic Sans", 40))
    labelantefinal.pack(pady=150)
    labelfinal = tk.Label(window, text=f"Tarefa: {tarefa}, Matéria: {materia}, Status: Pendente", font=("Comic Sans", 30))
    labelfinal.pack()

def adicionar_tarefa():
    label.pack(pady=10)
    tarefainput.pack(pady=20)
    label2.pack(pady=30)
    materiainput.pack(pady=20)
    buttom.pack(pady=30)

