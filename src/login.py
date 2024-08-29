import tkinter as tk
from tkinter import messagebox

from firebase_config import auth


def realizar_login():
    email = email_entry.get()
    senha = senha_entry.get()

    try:

        user = auth.sign_in_with_email_and_password(email, senha)
        messagebox.showinfo("SUCESSO", "LOGIN REALIZADO COM EXITO!")
        return user
    except:
        messagebox.showerror("ERRO", "FALHA AO FAZER LOGIN")
        return None


def tela_login():
    tela_login = tk.Toplevel()

    tela_login.title("LOGIN DO USUARIO")

    tela_login.width = 600
    tela_login.height = 600

    tk.Label(tela_login, text="email: ").grid(row=0, column=0)
    tk.Label(tela_login, text="senha: ").grid(row=1, column=0)

    global email_entry, senha_entry
    email_entry = tk.Entry(tela_login)
    senha_entry = tk.Entry(tela_login, show="*")

    email_entry.grid(row=0, column=1)
    senha_entry.grid(row=1, column=1)

    btn_login = tk.Button(tela_login, text="LOGIN", command=realizar_login)
    btn_login.grid(row=2, column=1, pady=10)



    tela_login.mainloop()
