import tkinter as tk
from tkinter import ttk


root = tk.Tk()


root.title('Perfil')


window_width = 1000
window_height = 1000


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


center_x = int(screen_width//2 - window_width//2)
center_y = int(screen_height//2 - window_height//2)


root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


root.resizable(False, False)


root.iconbitmap('.//assets/ic_ponto_do_carrinho.ico')


frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='').grid(column=0, row=0)

root.mainloop()