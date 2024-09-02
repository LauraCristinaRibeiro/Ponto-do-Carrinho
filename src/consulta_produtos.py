# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# Label = 0
#
# def mostrar_lista():
#
#     lista = ['iten 1', 'iten 2 ', 'iten 3']
#
#     texto = '\n'.join(lista)
#
#     Label.config(text=texto)
#
# def mostrar_resultado(root):
#     janela = tk.Frame(root)
#     resultado_label = tk.Listbox(janela)
#     resultado_label.pack(fill = tk.BOTH, expand = True)
#     return janela, resultado_label
#
#
#
# root = tk.Tk()
#
#
# root.title("CONSULTA PRODUTOS")
# #root.iconbitmap('./assets/ico.supermercado.ico')
# #root.iconbitmap("./assets/ic_ponto_do_carrinho.ico")
# entrada1 = tk.StringVar
# entratada2 = tk.StringVar
# entratada3 = tk.StringVar
# resultado = tk.StringVar
#
# tk.Label(root, text='DIGITE O NOME DO PRODUTO: ').grid(row=0, column=0)
# tk.Entry(root, textvariable=entrada1).grid(row=0, column=1)
#
#
#
# button_style1 = {
#     'font': ('Arial', 16),
#     'bg': '#d3d3d3',
#     'fg': '#0000FF',
#     'relief': 'raised',
#     'bd': 3,
#     'width': 10,
#     'height': 2
#
# }
#
# tk.Button(root, text="ADICIONAR" , command=entrada1, **button_style1).grid(row=3, column=0)
#
# button_style2 = {
#     'font': ('Arial', 16),
#     'bg': '#d3d3d3',
#     'fg': '#0000FF',
#     'relief': 'raised',
#     'bd': 3,
#     'width': 10,
#     'height': 2
#
# }
# tk.Button(root, text="DELETAR" , command=entratada2, **button_style2).grid(row=4, column=0)
#
# button_style3 = {
# 'font': ('Arial', 16),
#     'bg': '#d3d3d3',
#     'fg': '#0000FF',
#     'relief': 'raised',
#     'bd': 3,
#     'width': 10,
#     'height': 2
#
# }
# tk.Button(root, text="SAIR" , command=entratada2, **button_style2).grid(row=5, column=0)
#
#
#
# tk.Label(root, text="RESULTADO DO PRODUTO: ").grid(row=2, column=0)
# tk.Entry(root, textvariable=resultado, state='readonly').grid(row=2, column=1)
#
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from firebase_config import search_product

class PesquisaWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self, text="Nome do Produto:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(self, text="Pesquisar", command=self.search_product)
        self.search_button.pack()

        self.result_label = tk.Label(self, text="Resultados da Pesquisa:")
        self.result_label.pack()

        self.result_listbox = tk.Listbox(self)
        self.result_listbox.pack(fill=tk.BOTH, expand=True)

    def search_product(self):
        product_name = self.search_entry.get()
        if not product_name:
            messagebox.showerror("Erro", "Por favor, insira o nome de um produto.")
            return

        results = search_product(product_name)
        self.result_listbox.delete(0, tk.END)  # Limpa a lista antes de exibir novos resultados

        if results:
            for product in results:
                display_text = f"Nome: {product['name']}, Marca: {product['marca']}, Preço: R${product['price']:.2f}"
                self.result_listbox.insert(tk.END, display_text)
        else:
            messagebox.showinfo("Nenhum resultado", "Nenhum produto encontrado com esse nome.")
