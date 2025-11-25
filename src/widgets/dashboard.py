import tkinter as tk
from tkinter import messagebox
import sys
import os

# Simplified imports
from src.database.db_handler import init_db
from src.auth.login import login_user
from src.auth.register import register_user
from src.widgets.dashboard import Dashboard

def build_dashboard(root, username):
    """Create and show the dashboard"""
    # Hide the login window
    root.withdraw()
    
    # Create the Dashboard window (it's a Toplevel, so it creates its own window)
    dashboard = Dashboard(username)
    
    # When dashboard closes, close the entire app
    def on_dashboard_close():
        root.destroy()
    
    dashboard.protocol("WM_DELETE_WINDOW", on_dashboard_close)
    
    # Maximize the dashboard window
    try:
        dashboard.state('zoomed')  # Windows
    except:
        try:
            dashboard.attributes('-zoomed', True)  # Linux
        except:
            dashboard.geometry("1200x800")  # Fallback

def handle_login(root, username, password, login_frame):
    """Handle login attempt"""
    if login_user(username.get().strip(), password.get().strip()):
        messagebox.showinfo("Success", "Login successful!")
        build_dashboard(root, username.get().strip())
    else:
        messagebox.showerror("Error", "Invalid username or password")

def handle_register(username, password):
    """Handle registration attempt"""
    if register_user(username.get().strip(), password.get().strip()):
        messagebox.showinfo("Success", "Registration successful! You can now login.")
    else:
        messagebox.showerror("Error", "Registration failed. Username may already exist.")

def setup_login_ui(root):
    """Setup the login interface"""
    login_frame = tk.Frame(root, bg="#f5f5f5")
    login_frame.pack(fill="both", expand=True)

    # Title
    tk.Label(login_frame, 
            text="Secure Utilities",
            font=("Segoe UI", 24, "bold"),
            fg="#1a73e8",
            bg="#f5f5f5").pack(pady=(40,20))

    # Login container
    login_container = tk.Frame(login_frame, bg="#f5f5f5")
    login_container.pack(padx=40)

    # Username
    tk.Label(login_container, text="Username", bg="#f5f5f5", font=("Segoe UI", 10)).pack(anchor="w")
    username = tk.Entry(login_container, width=30, font=("Segoe UI", 10))
    username.pack(fill="x", pady=(0,15))

    # Password
    tk.Label(login_container, text="Password", bg="#f5f5f5", font=("Segoe UI", 10)).pack(anchor="w")
    password = tk.Entry(login_container, width=30, show="•", font=("Segoe UI", 10))
    password.pack(fill="x", pady=(0,5))

    # Show/Hide password
    show_pass = tk.BooleanVar()
    tk.Checkbutton(login_container, text="Show password",
                   bg="#f5f5f5",
                   variable=show_pass,
                   command=lambda: password.config(show="" if show_pass.get() else "•")
                   ).pack(anchor="w", pady=(0,15))

    # Buttons
    btn_frame = tk.Frame(login_container, bg="#f5f5f5")
    btn_frame.pack(fill="x", pady=15)

    login_btn = tk.Button(btn_frame, text="Login",
                         width=12,
                         font=("Segoe UI", 10, "bold"),
                         bg="#1a73e8", fg="white",
                         command=lambda: handle_login(root, username, password, login_frame))
    login_btn.grid(row=0, column=0, padx=5)

    register_btn = tk.Button(btn_frame, text="Register",
                            width=12,
                            font=("Segoe UI", 10),
                            command=lambda: handle_register(username, password))
    register_btn.grid(row=0, column=1, padx=5)

    # Configure button frame columns
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=1)

    # Bind enter key
    password.bind('<Return>', lambda e: handle_login(root, username, password, login_frame))
    username.bind('<Return>', lambda e: password.focus())

    return login_frame

def main():
    # Initialize database
    init_db()
    
    root = tk.Tk()
    root.title("Secure Utilities")
    root.geometry("420x380")
    root.config(bg="#f5f5f5")
    root.minsize(420, 380)
    
    # Center window
    window_width = 420
    window_height = 380
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Setup login UI
    setup_login_ui(root)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()