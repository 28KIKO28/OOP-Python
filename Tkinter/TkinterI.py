import tkinter as tk
from tkinter import mainloop as show

janela = tk.Tk()
janela.title("Stuff")
janela.geometry("1920x1080")

def printclick(texto):
    print(texto)
def close():
    janela.destroy()
def label(texto):
    label = tk.Label(janela, text=texto, font=("Creaking Crypt", 70), fg="Red")
    label.pack()
def imput(texto):
    entrada = tk.Entry(janela, font=("Creaking Crypt", 70), fg="Red")
    entrada.insert(0, texto)
    entrada.pack()
def butom(texto,açao):
    butom = tk.Button(janela, text=texto, font=("Creaking Crypt", 70), fg="Red", command=açao)
    butom.pack()

label("Queres realmente entrar?")
butom("Sim", printclick("Novo Morto!"))
butom("Não", close)
show()