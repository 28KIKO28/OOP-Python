import shutil as file
import os


imagens = "Imagens"
pdfs = "PDFs"
textos = "Texts"

os.makedirs(imagens, exist_ok=True)
os.makedirs(pdfs, exist_ok=True)
os.makedirs(textos, exist_ok=True)

def organizar(ficheiro):
    print(ficheiro)
    if ficheiro.endswith('.txt'):
        file.move(ficheiro, textos)
        print("Ficheiro movido para Texts!")
    elif ficheiro.endswith('.pdf'):
        file.move(ficheiro, pdfs)
        print("Ficheiro movido para PDFs!")
    elif ficheiro.endswith('.png'):
        file.move(ficheiro, imagens)
        print("Ficheiro movido para Imagens!")
    else:
        print("Não Coompreendido!")

files = input("Nome do ficheiro: ")
organizar(files)