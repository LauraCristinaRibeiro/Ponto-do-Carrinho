import tkinter as tk
from tkinter import messagebox

def realizar_confirmar():
    try:
       # user = auth.sign_in_with_email_and_password(email, senha)
        messagebox.showinfo("SUCESSO", "PRODUTO CADASTRADO COM SUCESSO!")
    except:
        messagebox.showerror("ERRO", "FALHA AO CADASTRAR PRODUTO")

def realizar_cadastro():
    entrada1 = tk.StringVar()
    entrada2 = tk.StringVar()
    entrada3 = tk.StringVar()
    resultado = tk.StringVar()

    realizar_cadastro = tk.Toplevel()

    tk.Label(realizar_cadastro, text="Cadastrar Produto: ").grid(row=0, column=0)
    tk.Entry(realizar_cadastro, textvariable=entrada1).grid(row=0, column=1)

    tk.Label(realizar_cadastro, text="Cadastrar Marca: ").grid(row=1, column=0)
    tk.Entry(realizar_cadastro, textvariable=entrada2).grid(row=1, column=1)

    tk.Label(realizar_cadastro, text="Cadastrar Preço: ").grid(row=2, column=0)
    tk.Entry(realizar_cadastro, textvariable=entrada3).grid(row=2, column=1)

    tk.Button(realizar_cadastro, text="Confirmar")
    btn_confirmar = tk.Button(realizar_cadastro, text="CONFIRMAR", command=realizar_confirmar)
    btn_confirmar.grid(row=3, column=1, pady=10)

    window_width = 300
    window_height = 200

    screen_width = realizar_cadastro.winfo_screenwidth()
    screen_height = realizar_cadastro.winfo_screenheight()

    center_x = int(screen_width//2 - window_width//2)
    center_y = int(screen_height//2 - window_height//2)

    realizar_cadastro.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    realizar_cadastro.resizable(False, False)

    realizar_cadastro.mainloop()