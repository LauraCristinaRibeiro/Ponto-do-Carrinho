import tkinter as tk
from tkinter import messagebox
Label = 0
def mostrar_lista():

    lista = ['iten 1', 'iten 2 ', 'iten 3']

    texto = '\n'.join(lista)

    Label.config(text=texto)


root = tk.Tk()

root.title("CONSULTA PRODUTOS")
#root.iconbitmap('./assets/ico.supermercado.ico')

entrada1 = tk.StringVar
entrtada2 = tk.StringVar
resultado = tk.StringVar

tk.Label(root, text='DIGITE O NOME DO PRODUTO: ').grid(row=0, column=0)
tk.Entry(root, textvariable=entrada1).grid(row=0, column=1)



button_style = {
    'font': ('Arial', 18),
    'bg': '#FFFF00',
    'fg': '#0000FF',
    'relief': 'raised',
    'bd': 3,
    'width': 3,
    'height': 2

}

tk.Button(root, text="D" , command=entrada1, **button_style).grid(row=3, column=0)


tk.Label(root, text="RESULTADO DO PRODUTO: ").grid(row=2, column=0)
tk.Entry(root, textvariable=resultado, state='readonly').grid(row=2, column=1)

root.mainloop()
