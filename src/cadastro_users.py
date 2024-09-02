import tkinter as tk
from firebase_config import add_user

class CadastroUsersWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Nome:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.cargo_label = tk.Label(self, text="Cargo:")
        self.cargo_label.pack()

        self.cargo_entry = tk.Entry(self)
        self.cargo_entry.pack()

        self.senha_label = tk.Label(self, text="Senha:")
        self.senha_label.pack()

        self.senha_entry = tk.Entry(self, show="*")
        self.senha_entry.pack()

        self.add_button = tk.Button(self, text="Cadastrar", command=self.add_user)
        self.add_button.pack()

    def add_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        cargo = self.cargo_entry.get()
        senha = self.senha_entry.get()
        add_user(name, email, cargo, senha)
        tk.messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
