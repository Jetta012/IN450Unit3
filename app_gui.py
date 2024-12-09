import tkinter as tk
from tkinter import messagebox
from business_layer import BusinessLayer

def login():
    server = server_entry.get()
    database = database_entry.get()
    user = username_entry.get()
    password = password_entry.get()

    try:
        # Initialize Business Layer
        business_layer = BusinessLayer(server, database, user, password)
        business_layer.connect()
        messagebox.showinfo("Login Successful", "Connected to the database!")
        open_main_window(business_layer)
    except Exception as e:
        messagebox.showerror("Login Failed", f"Error: {e}")

def open_main_window(business_layer):
    main_window = tk.Toplevel(root)
    main_window.title("Main Window")

    # Buttons for Queries
    tk.Button(main_window, text="Count IN450a", command=lambda: show_result("IN450a", business_layer.count_in450a())).pack(pady=10)
    tk.Button(main_window, text="View IN450b Names", command=lambda: show_result("IN450b Names", business_layer.get_in450b_names())).pack(pady=10)
    tk.Button(main_window, text="Count IN450c", command=lambda: show_result("IN450c", business_layer.count_in450c())).pack(pady=10)

def show_result(title, result):
    messagebox.showinfo(title, f"Result: {result}")

# Initialize GUI
root = tk.Tk()
root.title("Database Login")

# GUI Widgets for Login
tk.Label(root, text="Server:").grid(row=0, column=0, padx=10, pady=5)
server_entry = tk.Entry(root)
server_entry.grid(row=0, column=1)

tk.Label(root, text="Database:").grid(row=1, column=0, padx=10, pady=5)
database_entry = tk.Entry(root)
database_entry.grid(row=1, column=1)

tk.Label(root, text="Username:").grid(row=2, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=2, column=1)

tk.Label(root, text="Password:").grid(row=3, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

tk.Button(root, text="Login", command=login).grid(row=4, columnspan=2, pady=10)

root.mainloop()
