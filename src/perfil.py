import tkinter as tk

class PerfilWindow(tk.Frame):
    def __init__(self, master=None, user_data=None):
        super().__init__(master)
        self.master = master
        self.user_data = user_data
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text=f"Nome: {self.user_data['name']}")
        self.name_label.pack()

        self.email_label = tk.Label(self, text=f"Email: {self.user_data['email']}")
        self.email_label.pack()

        self.cargo_label = tk.Label(self, text=f"Cargo: {self.user_data['cargo']}")
        self.cargo_label.pack()
