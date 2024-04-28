import tkinter as tk
from tkinter import messagebox
from password_manager import check_credentials

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")
        self.login_button = tk.Button(self, text="Login", command=self.login)

        self.username_label.grid(row=0, column=0)
        self.username_entry.grid(row=0, column=1)
        self.password_label.grid(row=1, column=0)
        self.password_entry.grid(row=1, column=1)
        self.login_button.grid(row=2, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if check_credentials(username, password):
            self.controller.show_frame("MainPage")
        else:
            messagebox.showerror("Error", "Invalid username or password")

