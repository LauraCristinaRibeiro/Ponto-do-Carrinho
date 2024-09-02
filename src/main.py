# import tkinter as tk
# #from login import LoginWindow
# from cadastro_users import CadastroUsersWindow
# # #from cadastro_produtos import CadastroProdutosWindow
# # from consulta_produtos import PesquisaWindow
# # from perfil import PerfilWindow
#
# def main():
#     root = tk.Tk()
#     root.title("Ponto do Carrinho")
#     root.geometry("400x400")
#
#     def on_login_success(user_data):
#         for widget in root.winfo_children():
#             widget.destroy()
#
#         tk.Label(root, text=f"Bem-vindo, {user_data['name']}!").pack()
#
#         perfil_button = tk.Button(root, text="Perfil", command=lambda: open_perfil(user_data))
#         perfil_button.pack()
#
#         cadastro_produtos_button = tk.Button(root, text="Cadastrar Produto", command=open_cadastro_produtos)
#         cadastro_produtos_button.pack()
#
#         pesquisa_button = tk.Button(root, text="Pesquisar Produto", command=open_pesquisa)
#         pesquisa_button.pack()
#
#     def open_login():
#         for widget in root.winfo_children():
#             widget.destroy()
#         LoginWindow(root, on_login_success).pack()
#
#     def open_cadastro_users():
#         for widget in root.winfo_children():
#             widget.destroy()
#         CadastroUsersWindow(root).pack()
#
#     def open_cadastro_produtos():
#         for widget in root.winfo_children():
#             widget.destroy()
#         CadastroProdutosWindow(root).pack()
#
#     def open_pesquisa():
#         for widget in root.winfo_children():
#             widget.destroy()
#         PesquisaWindow(root).pack()
#
#     def open_perfil(user_data):
#         for widget in root.winfo_children():
#             widget.destroy()
#         PerfilWindow(root, user_data).pack()
#
#     # Menu Principal
#     login_button = tk.Button(root, text="Login", command=open_login)
#     login_button.pack()
#
#     cadastro_users_button = tk.Button(root, text="Cadastrar Usuário", command=open_cadastro_users)
#     cadastro_users_button.pack()
#
#     pesquisa_button = tk.Button(root, text="Pesquisar Produto", command=open_pesquisa)
#     pesquisa_button.pack()
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()

import tkinter as tk
from login import LoginWindow
from cadastro_users import CadastroUsersWindow
from cadastro_produtos import CadastroProdutosWindow
from consulta_produtos import PesquisaWindow
from perfil import PerfilWindow

def main():
    root = tk.Tk()
    root.title("Ponto do Carrinho")
    root.geometry("400x400")

    def on_login_success(user_data):
        for widget in root.winfo_children():
            widget.destroy()

        tk.Label(root, text=f"Bem-vindo, {user_data['name']}!").pack()

        perfil_button = tk.Button(root, text="Perfil", command=lambda: open_perfil(user_data))
        perfil_button.pack()

        cadastro_produtos_button = tk.Button(root, text="Cadastrar Produto", command=open_cadastro_produtos)
        cadastro_produtos_button.pack()

        pesquisa_button = tk.Button(root, text="Pesquisar Produto", command=open_pesquisa)
        pesquisa_button.pack()

    def open_login():
        for widget in root.winfo_children():
            widget.destroy()
        LoginWindow(root, on_login_success).pack()

    def open_cadastro_users():
        for widget in root.winfo_children():
            widget.destroy()
        CadastroUsersWindow(root).pack()

    def open_cadastro_produtos():
        for widget in root.winfo_children():
            widget.destroy()
        CadastroProdutosWindow(root).pack()

    def open_pesquisa():
        for widget in root.winfo_children():
            widget.destroy()
        PesquisaWindow(root).pack()

    def open_perfil(user_data):
        for widget in root.winfo_children():
            widget.destroy()
        PerfilWindow(root, user_data).pack()

    # Menu Principal
    login_button = tk.Button(root, text="Login", command=open_login)
    login_button.pack()

    cadastro_users_button = tk.Button(root, text="Cadastrar Usuário", command=open_cadastro_users)
    cadastro_users_button.pack()

    pesquisa_button = tk.Button(root, text="Pesquisar Produto", command=open_pesquisa)
    pesquisa_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()




