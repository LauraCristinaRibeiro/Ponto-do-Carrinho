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
        self.search_entry.config(width=60)
        self.search_entry.pack(pady=10)

        self.search_button = tk.Button(self, text="Pesquisar", command=self.search_product)
        self.search_button.pack(pady=10)

        self.result_label = tk.Label(self, text="Resultados da Pesquisa:")
        self.result_label.pack(pady=10)

        self.result_listbox = tk.Listbox(self)
        self.result_listbox.config(width=60,height=14)
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

