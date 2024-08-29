import tkinter as tk

from cadastro_users import tela_cadastro
from cadastro_produtos import telaCadProdutos
from login import tela_login
from perfil import mostrar_perfil

def tela_pincipal():
    # Create the main window
    tela_inicial = tk.Tk()
    tela_inicial.title("Tela Inicial")

    # Create a button that will call the tela_login function when clicked
    btn_inicializar_login = tk.Button(tela_inicial, text="Iniciar Login", command=tela_login)
    btn_inicializar_login.pack(pady=10)

    btn_inicializar_login = tk.Button(tela_inicial, text="cadastro", command=tela_cadastro)
    btn_inicializar_login.pack(pady=10)

    btn_inicializar_login = tk.Button(tela_inicial, text="cadastro produtos", command=telaCadProdutos)
    btn_inicializar_login.pack(pady=10)

    btn_inicializar_login = tk.Button(tela_inicial, text="mostrar perfil", command=mostrar_perfil)
    btn_inicializar_login.pack(pady=10)

    # Start the Tkinter event loop
    tela_inicial.mainloop()

if __name__ == "__main__":
    tela_pincipal()

