# import tkinter as tk
# from tkinter import ttk
# from firebase_config import recuperar_user
#
#
# def mostrar_perfil(user_id):
#     user_data = recuperar_user(user_id)
#     if (user_data):
#         root = tk.Tk()
#         root.title('Perfil')
#
#
#         label_nome = tk.Label(root,text=f"Nome: {user_data['nome']}")
#         label_nome.pack(pady=10)
#
#         label_email = tk.Label(root,text=f"Email: {user_data['email']}")
#         label_email.pack(pady=10)
#
#
#         label_cargo = tk.Label(root,text=f"Cargo: {user_data['cargo']}")
#         label_cargo.pack(pady=10)
#
#
#         window_width = 1000
#         window_height = 1000
#
#
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#
#
#         center_x = int(screen_width//2 - window_width//2)
#         center_y = int(screen_height//2 - window_height//2)
#
#
#         root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
#
#
#         root.resizable(False, False)
#
#
#         root.iconbitmap('.//assets/ic_ponto_do_carrinho.ico')
#
#
#         frm = ttk.Frame(root, padding=10)
#         frm.grid()
#         ttk.Label(frm, text='').grid(column=0, row=0)
#
#         root.mainloop()
#
#     else:
#         print("Erro ao recuperar dados do usuário")

import tkinter as tk


class PerfilWindow(tk.Frame):
    def __init__(self, master=None, user_data=None):
        super().__init__(master)
        self.master = master
        self.user_data = user_data
        self.create_widgets()


def create_widgets(self):
    self.name_label = tk.Label(self, text=f&quot;Nome: {self.user_data[&#39;name&#39;]}&quot;)
    self.name_label.pack()


    self.email_label = tk.Label(self, text=f&quot;Email: {self.user_data[&#39;email&#39;]}&quot;)
    self.email_label.pack()

    self.cargo_label = tk.Label(self, text=f&quot;Cargo: {self.user_data[&#39;cargo&#39;]}&quot;)
    self.cargo_label.pack()