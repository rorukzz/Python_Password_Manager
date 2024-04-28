import tkinter as tk
from tkinter import messagebox
import csv
from cryptography.fernet import Fernet

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Label for the main page
        label = tk.Label(self, text="Main Page")
        label.pack()

        # Button to logout
        logout_button = tk.Button(self, text="Logout", command=self.logout)
        logout_button.pack()

        # Listbox to display passwords
        self.password_listbox = tk.Listbox(self)
        self.password_listbox.pack()

        # Button to add new password
        add_button = tk.Button(self, text="Add Password", command=self.controller.show_add_password)
        add_button.pack()

        # Load passwords from CSV
        self.load_passwords()

    def load_passwords(self):
        try:
            with open('passwords.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.password_listbox.insert(tk.END, row[0])  # Display only titles
        except FileNotFoundError:
            messagebox.showerror("Error", "Password file not found.")

    def logout(self):
        self.controller.show_frame("LoginPage")

class AddPasswordPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Entry fields for new password entry
        title_label = tk.Label(self, text="Title:")
        title_label.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        username_label = tk.Label(self, text="Username:")
        username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        password_label = tk.Label(self, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        # Button to add new password
        add_button = tk.Button(self, text="Add Password", command=self.add_password)
        add_button.pack()

        # Button to go back to main page
        back_button = tk.Button(self, text="Back", command=self.go_to_main_page)
        back_button.pack()

    def add_password(self):
        title = self.title_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not title or not username or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Generate key for encryption
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        # Encrypt username and password
        encrypted_username = cipher_suite.encrypt(username.encode()).decode()
        encrypted_password = cipher_suite.encrypt(password.encode()).decode()

        try:
            with open('passwords.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title, encrypted_username, encrypted_password])
            messagebox.showinfo("Success", "Password added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add password: {str(e)}")

        # Clear input fields
        self.title_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def go_to_main_page(self):
        self.controller.show_frame("MainPage")
