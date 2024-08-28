##Cadastro_Users
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.firebase_config import auth, db


def cadastrar_usuario(email, senha, nome, cargo):
    try:
        user = auth.create_user_with_email_and_password(email, senha)
        uid = user['localId']
        #criar o documento com o UID com ID
        db.collection('users').document(uid).set({
            "nome": nome,
            "email": email,
            "cargo": cargo
        })
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso")
        return uid
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao cadastrar usuário. {e}")
        return None


def tela_cadastro():


    root_cadasto = tk.Toplevel()
    root_cadasto.title("Cadastro de Usuários")
    # frm = ttk.Frame(root_cadasto, padding=10)
    # frm.grid()
    # ttk.Label(frm, text="Cadastro de users!").grid(column=0, row=0)


    tk.Label(root_cadasto, text="Nome: ").grid(row=1, column=0)
    nome_entry = tk.Entry(root_cadasto)
    nome_entry.grid(row=1, column=1)

    tk.Label(root_cadasto, text="Email: ").grid(row=2, column=0)
    email_entry = tk.Entry(root_cadasto)
    email_entry.grid(row=2, column=1)

    tk.Label(root_cadasto, text="Cargo: ").grid(row=3, column=0)
    cargo_entry = tk.Entry(root_cadasto)
    cargo_entry.grid(row=3, column=1)

    tk.Label(root_cadasto, text="Senha: ").grid(row=4, column=0)
    senha_entry = tk.Entry(root_cadasto, show="*")
    senha_entry.grid(row=4, column=1)

    ttk.Button(root_cadasto, text="Next", command=cadastrar_usuario).grid(column=1, row=5)
    root_cadasto.mainloop()

