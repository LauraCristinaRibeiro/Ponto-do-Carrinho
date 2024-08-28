import tkinter as tk


from login import tela_login


def tela_pincipal():
    # Create the main window
    tela_inicial = tk.Tk()
    tela_inicial.title("Tela Inicial")

    # Create a button that will call the tela_login function when clicked
    btn_inicializar_login = tk.Button(tela_inicial, text="Iniciar Login", command=tela_login)
    btn_inicializar_login.pack(pady=10)

    btn_inicializar_login = tk.Button(tela_inicial, text="cadastro", command=cadastro_users.tela_cadastro)
    btn_inicializar_login.pack(pady=10)

    btn_inicializar_login = tk.Button(tela_inicial, text="cadastro produtos", command=cadastro_produtos.telaCadProdutos)
    btn_inicializar_login.pack(pady=10)


    # Start the Tkinter event loop
    tela_inicial.mainloop()

if __name__ == "__main__":
    tela_pincipal()

