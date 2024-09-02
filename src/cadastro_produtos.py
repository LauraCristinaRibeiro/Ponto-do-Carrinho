# import tkinter as tk
# from tkinter import messagebox
#
# def realizar_confirmar():
#     try:
#        # user = auth.sign_in_with_email_and_password(email, senha)
#         messagebox.showinfo("SUCESSO", "PRODUTO CADASTRADO COM SUCESSO!")
#     except:
#         messagebox.showerror("ERRO", "FALHA AO CADASTRAR PRODUTO")
#
#
# def add_produto(nome, marca, preco):
#   produto_ref = db.collection('produtos').document()
#   produto_ref.set({
#     'nome': nome,
#     'marca': marca,
#     'preco': preco
#   })
#
# def realizar_cadastro():
#     entrada1 = tk.StringVar()
#     entrada2 = tk.StringVar()
#     entrada3 = tk.StringVar()
#     resultado = tk.StringVar()
#
#
#     realizar_cadastro = tk.Toplevel()
#
#     tk.Label(realizar_cadastro, text="Cadastrar Produto: ").grid(row=0, column=0)
#     tk.Entry(realizar_cadastro, textvariable=entrada1).grid(row=0, column=1)
#
#     tk.Label(realizar_cadastro, text="Cadastrar Marca: ").grid(row=1, column=0)
#     tk.Entry(realizar_cadastro, textvariable=entrada2).grid(row=1, column=1)
#
#     tk.Label(realizar_cadastro, text="Cadastrar Preço: ").grid(row=2, column=0)
#     tk.Entry(realizar_cadastro, textvariable=entrada3).grid(row=2, column=1)
#
#     tk.Button(realizar_cadastro, text="Confirmar")
#     btn_confirmar = tk.Button(realizar_cadastro, text="CONFIRMAR", command=realizar_confirmar)
#     btn_confirmar.grid(row=3, column=1, pady=10)
#
#     window_width = 300
#     window_height = 200
#
#     screen_width = realizar_cadastro.winfo_screenwidth()
#     screen_height = realizar_cadastro.winfo_screenheight()
#
#     center_x = int(screen_width//2 - window_width//2)
#     center_y = int(screen_height//2 - window_height//2)
#
#     realizar_cadastro.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#
#     realizar_cadastro.resizable(False, False)
#
#     realizar_cadastro.mainloop()

import tkinter as tk
from firebase_config import add_product

class CadastroProdutosWindow(tk.Frame):
def __init__(self, master=None):
super().__init__(master)
self.master = master
self.create_widgets()

def create_widgets(self):
self.name_label = tk.Label(self, text=&quot;Nome do Produto:&quot;)
self.name_label.pack()

self.name_entry = tk.Entry(self)
self.name_entry.pack()

self.marca_label = tk.Label(self, text=&quot;Marca:&quot;)
self.marca_label.pack()

self.marca_entry = tk.Entry(self)
self.marca_entry.pack()

self.price_label = tk.Label(self, text=&quot;Preço:&quot;)
self.price_label.pack()

self.price_entry = tk.Entry(self)
self.price_entry.pack()

self.add_button = tk.Button(self, text=&quot;Cadastrar&quot;, command=self.add_product)
self.add_button.pack()

def add_product(self):
name = self.name_entry.get()
marca = self.marca_entry.get()
price = float(self.price_entry.get())
add_product(name, marca, price)
tk.messagebox.showinfo(&quot;Sucesso&quot;, &quot;Produto cadastrado com sucesso!&quot;)