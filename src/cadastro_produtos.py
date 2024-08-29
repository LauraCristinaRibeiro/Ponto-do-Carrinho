import tkinter as tk
from tkinter import messagebox
telaCadProdutos = tk.Tk()

entrada1 = tk.StringVar()
entrada2 = tk.StringVar()
entrada3 = tk.StringVar()
resultado = tk.StringVar()

telaCadProdutos.title('PRODUTOS PONTO DO CARRINHO')

tk.Label(telaCadProdutos, text="Cadastrar Produto: ").grid(row=0, column=0)
tk.Entry(telaCadProdutos, textvariable=entrada1).grid(row=0, column=1)

tk.Label(telaCadProdutos, text="Cadastrar Marca: ").grid(row=1, column=0)
tk.Entry(telaCadProdutos, textvariable=entrada2).grid(row=1, column=1)

tk.Label(telaCadProdutos, text="Cadastrar Preço: ").grid(row=2, column=0)
tk.Entry(telaCadProdutos, textvariable=entrada3).grid(row=2, column=1)

tk.Button(telaCadProdutos, text="Confirmar")

def realizar_confirmar():

    try:
       # user = auth.sign_in_with_email_and_password(email, senha)
        messagebox.showinfo("SUCESSO", "PRODUTO CADASTRADO COM SUCESSO!")
    except:
        messagebox.showerror("ERRO", "FALHA AO CADASTRAR PRODUTO")


btn_confirmar = tk.Button(telaCadProdutos, text="CONFIRMAR", command=realizar_confirmar)
btn_confirmar.grid(row=3, column=1, pady=10)

window_width = 300
window_height = 200

screen_width = telaCadProdutos.winfo_screenwidth()
screen_height = telaCadProdutos.winfo_screenheight()

center_x = int(screen_width//2 - window_width//2)
center_y = int(screen_height//2 - window_height//2)

telaCadProdutos.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

telaCadProdutos.resizable(False, False)

telaCadProdutos.mainloop()