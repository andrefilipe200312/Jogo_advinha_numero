import random
import tkinter as tk
from tkinter import messagebox

def verificar_numero():
    numero = int(entrada.get())
    if numero == i:
        messagebox.showinfo("Resultado", "Você acertou!")
        janela.quit()
    else:
        messagebox.showinfo("Resultado", "Não acertou!")

i = random.randint(0, 10)

janela = tk.Tk()
janela.title("Jogo Advinha Numero")

label=tk.Label(janela, text="Digite um numero inteiro entre 0-10:")
label.pack()

entrada=tk.Entry(janela)
entrada.pack()

botao=tk.Button(janela,text="Verificar", command = verificar_numero)
botao.pack()

janela.mainloop()