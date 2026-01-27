import tkinter as tk
import json
import os
from DEFs import adicionar_tarefa
from DEFs import labelcreator
tarefa = ""
materia = ""
status = ""

window = tk.Tk()
window.title("Minhas Tarefas")
window.geometry("1920x1080")
window.iconbitmap("Icon.ico") 
labelcreator()

meu_arquivo = tk.Menu(window)
menu_arquivo = tk.Menu(meu_arquivo, tearoff=0)
menu_arquivo.add_command(label="Novo", command=lambda:adicionar_tarefa())
menu_arquivo.add_command(label="Remover")
menu_arquivo.add_command(label="Concluir")
meu_arquivo.add_cascade(label="Arquivo", menu=menu_arquivo)
window.config(menu=meu_arquivo)
window.mainloop()