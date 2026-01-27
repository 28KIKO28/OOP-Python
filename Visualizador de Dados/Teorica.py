import matplotlib.pyplot as plt

materia = ["Matemática", "Física", "Química"]

concluidas = [5, 3, 4]

plt.pie(concluidas, labels=materia, autopct="%1.1f%%")
plt.title("Horas estudadas por materia")
plt.show()