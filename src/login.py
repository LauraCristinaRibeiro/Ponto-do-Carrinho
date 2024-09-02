import tkinter as tk
from tkinter import messagebox
from firebase_config import get_user

class LoginWindow(tk.Frame):
    def __init__(self, master=None, on_login_success=None):
        super().__init__(master)
        self.master = master
        self.on_login_success = on_login_success
        self.create_widgets()

    def create_widgets(self):
        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.password_label = tk.Label(self, text="Senha:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.check_login)
        self.login_button.pack()

    def check_login(self):
        email = self.email_entry.get()
        senha = self.password_entry.get()
        user = get_user(email)
        if user and user['senha'] == senha:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            if self.on_login_success:
                self.on_login_success(user)
        else:
            messagebox.showerror("Erro", "Credenciais inválidas!")
