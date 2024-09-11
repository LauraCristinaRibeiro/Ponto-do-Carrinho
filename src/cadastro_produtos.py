import tkinter as tk
from firebase_config import add_product

class CadastroProdutosWindow(tk.Frame):
    def __init__(self, master=None, go_home_callback=None):
        super().__init__(master)
        self.master = master
        self.go_home_callback = go_home_callback
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Nome do Produto:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.marca_label = tk.Label(self, text="Marca:")
        self.marca_label.pack()

        self.marca_entry = tk.Entry(self)
        self.marca_entry.pack()

        self.price_label = tk.Label(self, text="Preço:")
        self.price_label.pack()

        self.price_entry = tk.Entry(self)
        self.price_entry.pack()

        self.add_button = tk.Button(self, text="Cadastrar", command=self.add_product)
        self.add_button.pack()



    def add_product(self):
        name = self.name_entry.get()
        marca = self.marca_entry.get()
        price = float(self.price_entry.get())
        add_product(name, marca, price)
        tk.messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")



