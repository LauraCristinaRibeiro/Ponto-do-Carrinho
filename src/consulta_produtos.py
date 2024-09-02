import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
Label = 0

def mostrar_lista():

    lista = ['iten 1', 'iten 2 ', 'iten 3']

    texto = '\n'.join(lista)

    Label.config(text=texto)

def mostrar_resultado(root):
    janela = tk.Frame(root)
    resultado_label = tk.Listbox(janela)
    resultado_label.pack(fill = tk.BOTH, expand = True)
    return janela, resultado_label



root = tk.Tk()


root.title("CONSULTA PRODUTOS")
#root.iconbitmap('./assets/ico.supermercado.ico')
#root.iconbitmap("./assets/ic_ponto_do_carrinho.ico")
entrada1 = tk.StringVar
entratada2 = tk.StringVar
entratada3 = tk.StringVar
resultado = tk.StringVar

tk.Label(root, text='DIGITE O NOME DO PRODUTO: ').grid(row=0, column=0)
tk.Entry(root, textvariable=entrada1).grid(row=0, column=1)



button_style1 = {
    'font': ('Arial', 16),
    'bg': '#d3d3d3',
    'fg': '#0000FF',
    'relief': 'raised',
    'bd': 3,
    'width': 10,
    'height': 2

}

tk.Button(root, text="ADICIONAR" , command=entrada1, **button_style1).grid(row=3, column=0)

button_style2 = {
    'font': ('Arial', 16),
    'bg': '#d3d3d3',
    'fg': '#0000FF',
    'relief': 'raised',
    'bd': 3,
    'width': 10,
    'height': 2

}
tk.Button(root, text="DELETAR" , command=entratada2, **button_style2).grid(row=4, column=0)

button_style3 = {
'font': ('Arial', 16),
    'bg': '#d3d3d3',
    'fg': '#0000FF',
    'relief': 'raised',
    'bd': 3,
    'width': 10,
    'height': 2

}
tk.Button(root, text="SAIR" , command=entratada2, **button_style2).grid(row=5, column=0)



tk.Label(root, text="RESULTADO DO PRODUTO: ").grid(row=2, column=0)
tk.Entry(root, textvariable=resultado, state='readonly').grid(row=2, column=1)

root.mainloop()
