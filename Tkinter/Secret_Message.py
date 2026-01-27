import tkinter as tk
from tkinter import mainloop as show

window = tk.Tk()
window.title("Secret Message")
window.geometry("1920x1080")
window.iconbitmap("Image.ico")

label= tk.Label(window, font=("Creaking Crypt", 70), fg="Red")
label.pack()



def massage():
    label.config(text="Now you can't run!")
    buttom.destroy()

label= tk.Label(window, text="Press the buttom if you dare!", font=("Creaking Crypt", 70), fg="Red")
label.pack()
buttom = tk.Button(window, text="Do you dare?", font=("Creaking Crypt", 70), fg="Red", command=massage)
buttom.pack()


show()
