import tkinter as tk
from tkinter import mainloop as show
from tkinter import *

window = tk.Tk()
window.title("Colour Picking")
window.geometry("1920x1080")
window.configure(background="white")

def pick_colour(wich):
    if wich == 1:
        window.configure(bg="red")
        buttom3.config(bg="red")
    elif wich == 2:
        window.configure(bg="blue")
        buttom3.config(bg="blue")
    elif wich == 3:
        window.configure(bg="green")
        buttom3.config(bg="green")
    elif wich == 0:
        label.destroy()
        buttom.destroy()
        buttom1.destroy()
        buttom2.destroy()
        buttom3.destroy()
        window.configure(bg="white")
        image = PhotoImage(file="C:/Users/FranciscoNicolau/Tkinter/SigmaFace.png")
        image_label = tk.Label(window, image=image, bg="white", borderwidth=0)
        image_label.pack(pady=350)
        show()

label = tk.Label(window, text=f"Wich Colour You Want to Pick?", font=("Times New Roman", 60), fg="Black")
label.pack()
buttom = tk.Button(window, text="VERMELHO", font=("Times New Roman", 60), fg="Red", borderwidth=0, command=lambda: pick_colour(wich=1))
buttom.pack(pady=50)
buttom1 = tk.Button(window, text="AZUL", font=("Times New Roman", 60), fg="Blue", borderwidth=0, command=lambda: pick_colour(wich=2))
buttom1.pack(pady=50)
buttom2 = tk.Button(window, text="VERDE", font=("Times New Roman", 60), fg="Green", borderwidth=0, command=lambda: pick_colour(wich=3))
buttom2.pack(pady=50)
buttom3 = tk.Button(window, text="", font=("Times New Roman", 60), fg="Black", borderwidth=0, command=lambda: pick_colour(wich=0))
buttom3.pack(pady=50)

show()