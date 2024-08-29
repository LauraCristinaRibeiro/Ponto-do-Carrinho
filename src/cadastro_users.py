##Cadastro_Users
import tkinter as tk
from tkinter import *
from tkinter import ttk

def tela_cadastro():

    window_width = 300
    window_height = 200
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Cadastro de users!").grid(column=0, row=0)

    email_entry = tk.Entry(root)
    senha_entry = tk.Entry(root, show="*")

    tk.Label(root, text="Email: ").grid(row=1, column=0)
    email_entry.grid(row=1, column= 1)

    tk.Label(root, text="Senha: ").grid(row=2, column=0)
    senha_entry.grid(row= 2, column= 1)


    ttk.Button(frm, text="Next", command=root.destroy).grid(column=1, row=3)
    root.mainloop()