import tkinter as tk
from tkinter import mainloop as show

window = tk.Tk()
window.title("Clicker Counting")
window.geometry("1920x1080")

count = 0

def update_count():
    global count
    count += 1
    print(count)
    label.config(text=f"Cliks: {count}")
    if count == 10:
        label2.config(text="Noob Cliker!")
    elif count == 50:
        label2.config(text="Impressive clicking!")
    elif count == 100: 
        label2.config(text="Clicking Master!")
    elif count == 200:
        label2.config(text="Unstoppable Clicker!")
    elif count == 300:
        label2.config(text="Legendary Clicker!")
        buttom.config(state="disabled", text="Max Clicks", fg="red", font=("Creaking Crypt", 40), padx=50, pady=20, bg="black", relief="sunken", bd=10, cursor="X_cursor")
    
label= tk.Label(window, text=f"Cliks: 0", font=("Creaking Crypt", 60), fg="Red")
label.pack(pady=150)
buttom = tk.Button(window, text="Click Me!", font=("Creaking Crypt", 60), fg="Red", command=update_count)
buttom.pack(pady=50, padx=800)
label2 = tk.Label(window, text="", font=("Creaking Crypt", 60), fg="Red")
label2.pack(pady=50)

show()
while True:  
    buttom.bind("<Button-1>", lambda event: update_count())
    show()