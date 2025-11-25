import tkinter as tk
from tkinter import messagebox
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Simplified imports
from src.database.db_handler import init_db
from src.auth.login import login_user
from src.auth.register import register_user
from src.utilities_menu import build_dashboard

# Professional Black/Yellow/White color scheme
COLORS = {
    'black': '#1a1a1a',
    'dark_gray': '#2d2d2d',
    'yellow': '#ffd700',
    'yellow_dark': '#ccac00',
    'white': '#ffffff',
    'light_gray': '#f5f5f5',
    'text_dark': '#1a1a1a',
    'border': '#e0e0e0'
}

def show_dashboard(root, username):
    """Create and show the dashboard"""
    print(f"DEBUG: Building dashboard for {username}")
    
    try:
        # Clear the login screen
        for widget in root.winfo_children():
            widget.destroy()
        
        # Build the accessible dashboard directly in the root window
        dashboard = build_dashboard(root, username)
        
        print("DEBUG: Dashboard created successfully")
        
    except Exception as e:
        print(f"ERROR: Failed to create dashboard: {e}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error", f"Failed to create dashboard: {e}")

def handle_login(root, username_entry, password_entry):
    """Handle login attempt"""
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    
    print(f"DEBUG: Login attempt for user: {username}")
    
    if login_user(username, password):
        messagebox.showinfo("Success", "Login successful!")
        show_dashboard(root, username)
    else:
        messagebox.showerror("Error", "Invalid username or password")
        password_entry.delete(0, tk.END)

def handle_register(username_entry, password_entry, confirm_entry):
    """Handle registration attempt"""
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    confirm = confirm_entry.get().strip()
    
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password")
        return
    
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match!")
        return
    
    if len(password) < 6:
        messagebox.showerror("Error", "Password must be at least 6 characters long")
        return
    
    print(f"DEBUG: Registration attempt for user: {username}")
    
    if register_user(username, password):
        messagebox.showinfo("Success", "Registration successful! You can now login.")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Registration failed. Username may already exist.")

def show_register_form(root, login_container):
    """Show registration form"""
    # Clear login container
    for widget in login_container.winfo_children():
        widget.destroy()
    
    # Registration header
    header_frame = tk.Frame(login_container, bg=COLORS['light_gray'])
    header_frame.pack(fill="x", pady=(0, 30))
    
    tk.Label(header_frame,
            text="Create Account",
            font=("Segoe UI", 24, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['black']).pack(pady=(0, 5))
    
    tk.Label(header_frame,
            text="Join Secure Utilities today",
            font=("Segoe UI", 11),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack()
    
    # Form fields
    form = tk.Frame(login_container, bg=COLORS['light_gray'])
    form.pack(fill="both", expand=True, padx=40)
    
    # Username
    tk.Label(form,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(anchor="w", pady=(0, 5))
    
    username_frame = tk.Frame(form, bg=COLORS['border'], bd=1)
    username_frame.pack(fill="x", pady=(0, 20))
    
    username_entry = tk.Entry(username_frame,
                              font=("Segoe UI", 11),
                              relief="flat",
                              bg="white",
                              fg=COLORS['text_dark'])
    username_entry.pack(fill="x", padx=2, pady=2, ipady=10, ipadx=10)
    username_entry.focus()
    
    # Password
    tk.Label(form,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(anchor="w", pady=(0, 5))
    
    password_frame = tk.Frame(form, bg=COLORS['border'], bd=1)
    password_frame.pack(fill="x", pady=(0, 20))
    
    password_entry = tk.Entry(password_frame,
                             font=("Segoe UI", 11),
                             relief="flat",
                             bg="white",
                             fg=COLORS['text_dark'],
                             show="●")
    password_entry.pack(fill="x", padx=2, pady=2, ipady=10, ipadx=10)
    
    # Confirm Password
    tk.Label(form,
            text="Confirm Password",
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(anchor="w", pady=(0, 5))
    
    confirm_frame = tk.Frame(form, bg=COLORS['border'], bd=1)
    confirm_frame.pack(fill="x", pady=(0, 10))
    
    confirm_entry = tk.Entry(confirm_frame,
                            font=("Segoe UI", 11),
                            relief="flat",
                            bg="white",
                            fg=COLORS['text_dark'],
                            show="●")
    confirm_entry.pack(fill="x", padx=2, pady=2, ipady=10, ipadx=10)
    
    # Show password checkbox
    show_var = tk.BooleanVar()
    def toggle_password():
        if show_var.get():
            password_entry.config(show="")
            confirm_entry.config(show="")
        else:
            password_entry.config(show="●")
            confirm_entry.config(show="●")
    
    tk.Checkbutton(form,
                  text="Show password",
                  bg=COLORS['light_gray'],
                  fg=COLORS['text_dark'],
                  font=("Segoe UI", 9),
                  activebackground=COLORS['light_gray'],
                  variable=show_var,
                  command=toggle_password).pack(anchor="w", pady=(0, 25))
    
    # Register button
    register_btn = tk.Button(form,
                            text="Create Account",
                            font=("Segoe UI", 12, "bold"),
                            bg=COLORS['yellow'],
                            fg=COLORS['black'],
                            relief="flat",
                            cursor="hand2",
                            command=lambda: handle_register(username_entry, password_entry, confirm_entry))
    register_btn.pack(fill="x", ipady=12, pady=(0, 20))
    
    # Hover effects
    register_btn.bind("<Enter>", lambda e: register_btn.config(bg=COLORS['yellow_dark']))
    register_btn.bind("<Leave>", lambda e: register_btn.config(bg=COLORS['yellow']))
    
    # Back to login
    back_frame = tk.Frame(form, bg=COLORS['light_gray'])
    back_frame.pack(pady=10)
    
    tk.Label(back_frame,
            text="Already have an account?",
            font=("Segoe UI", 9),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(side="left", padx=(0, 5))
    
    back_btn = tk.Button(back_frame,
                        text="Sign In",
                        font=("Segoe UI", 9, "bold"),
                        bg=COLORS['light_gray'],
                        fg=COLORS['yellow_dark'],
                        relief="flat",
                        cursor="hand2",
                        bd=0,
                        command=lambda: setup_login_ui(root))
    back_btn.pack(side="left")
    
    # Bind enter key
    confirm_entry.bind('<Return>', lambda e: handle_register(username_entry, password_entry, confirm_entry))

def setup_login_ui(root):
    """Setup the professional login interface"""
    # Clear root
    for widget in root.winfo_children():
        widget.destroy()
    
    # Main container with split design
    main_container = tk.Frame(root, bg=COLORS['black'])
    main_container.pack(fill="both", expand=True)
    
    # Left side - Brand/Image section
    left_side = tk.Frame(main_container, bg=COLORS['black'], width=400)
    left_side.pack(side="left", fill="both", expand=True)
    left_side.pack_propagate(False)
    
    # Center content in left side
    left_content = tk.Frame(left_side, bg=COLORS['black'])
    left_content.place(relx=0.5, rely=0.5, anchor="center")
    
    # Logo/Icon (using emoji as placeholder)
    tk.Label(left_content,
            text="🔐",
            font=("Segoe UI", 80),
            bg=COLORS['black'],
            fg=COLORS['yellow']).pack(pady=(0, 20))
    
    tk.Label(left_content,
            text="SECURE UTILITIES",
            font=("Segoe UI", 26, "bold"),
            bg=COLORS['black'],
            fg=COLORS['white']).pack(pady=(0, 10))
    
    tk.Label(left_content,
            text="Your all-in-one toolkit",
            font=("Segoe UI", 12),
            bg=COLORS['black'],
            fg=COLORS['yellow']).pack()
    
    # Decorative elements
    features = ["🔗 URL Shortener", "🔢 Calculator", "💬 Messaging", "📊 Data Generator"]
    features_frame = tk.Frame(left_content, bg=COLORS['black'])
    features_frame.pack(pady=(40, 0))
    
    for feature in features:
        tk.Label(features_frame,
                text=feature,
                font=("Segoe UI", 10),
                bg=COLORS['black'],
                fg=COLORS['white']).pack(pady=5)
    
    # Right side - Login form
    right_side = tk.Frame(main_container, bg=COLORS['light_gray'], width=500)
    right_side.pack(side="right", fill="both")
    right_side.pack_propagate(False)
    
    # Login container (centered)
    login_container = tk.Frame(right_side, bg=COLORS['light_gray'])
    login_container.place(relx=0.5, rely=0.5, anchor="center", width=400)
    
    # Login header
    tk.Label(login_container,
            text="Welcome Back",
            font=("Segoe UI", 24, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['black']).pack(pady=(0, 5))
    
    tk.Label(login_container,
            text="Sign in to continue",
            font=("Segoe UI", 11),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(pady=(0, 40))
    
    # Username field
    tk.Label(login_container,
            text="Username",
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(anchor="w", pady=(0, 5))
    
    username_frame = tk.Frame(login_container, bg=COLORS['border'], bd=1)
    username_frame.pack(fill="x", pady=(0, 20))
    
    username_entry = tk.Entry(username_frame,
                              font=("Segoe UI", 11),
                              relief="flat",
                              bg="white",
                              fg=COLORS['text_dark'])
    username_entry.pack(fill="x", padx=2, pady=2, ipady=10, ipadx=10)
    username_entry.focus()
    
    # Password field
    tk.Label(login_container,
            text="Password",
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(anchor="w", pady=(0, 5))
    
    password_frame = tk.Frame(login_container, bg=COLORS['border'], bd=1)
    password_frame.pack(fill="x", pady=(0, 10))
    
    password_entry = tk.Entry(password_frame,
                             font=("Segoe UI", 11),
                             relief="flat",
                             bg="white",
                             fg=COLORS['text_dark'],
                             show="●")
    password_entry.pack(fill="x", padx=2, pady=2, ipady=10, ipadx=10)
    
    # Show password checkbox
    show_var = tk.BooleanVar()
    tk.Checkbutton(login_container,
                  text="Show password",
                  bg=COLORS['light_gray'],
                  fg=COLORS['text_dark'],
                  font=("Segoe UI", 9),
                  activebackground=COLORS['light_gray'],
                  variable=show_var,
                  command=lambda: password_entry.config(show="" if show_var.get() else "●")).pack(anchor="w", pady=(0, 30))
    
    # Login button
    login_btn = tk.Button(login_container,
                         text="Sign In",
                         font=("Segoe UI", 12, "bold"),
                         bg=COLORS['yellow'],
                         fg=COLORS['black'],
                         relief="flat",
                         cursor="hand2",
                         command=lambda: handle_login(root, username_entry, password_entry))
    login_btn.pack(fill="x", ipady=12, pady=(0, 20))
    
    # Hover effect
    login_btn.bind("<Enter>", lambda e: login_btn.config(bg=COLORS['yellow_dark']))
    login_btn.bind("<Leave>", lambda e: login_btn.config(bg=COLORS['yellow']))
    
    # Divider
    divider_frame = tk.Frame(login_container, bg=COLORS['light_gray'])
    divider_frame.pack(fill="x", pady=15)
    
    tk.Frame(divider_frame, bg=COLORS['border'], height=1).pack(side="left", fill="x", expand=True)
    tk.Label(divider_frame,
            text="OR",
            font=("Segoe UI", 9),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(side="left", padx=10)
    tk.Frame(divider_frame, bg=COLORS['border'], height=1).pack(side="left", fill="x", expand=True)
    
    # Register link
    register_frame = tk.Frame(login_container, bg=COLORS['light_gray'])
    register_frame.pack(pady=15)
    
    tk.Label(register_frame,
            text="Don't have an account?",
            font=("Segoe UI", 9),
            bg=COLORS['light_gray'],
            fg=COLORS['text_dark']).pack(side="left", padx=(0, 5))
    
    register_btn = tk.Button(register_frame,
                            text="Create Account",
                            font=("Segoe UI", 9, "bold"),
                            bg=COLORS['light_gray'],
                            fg=COLORS['yellow_dark'],
                            relief="flat",
                            cursor="hand2",
                            bd=0,
                            command=lambda: show_register_form(root, login_container))
    register_btn.pack(side="left")
    
    # Bind enter key
    password_entry.bind('<Return>', lambda e: handle_login(root, username_entry, password_entry))
    username_entry.bind('<Return>', lambda e: password_entry.focus())

def main():
    # Initialize database
    init_db()
    
    root = tk.Tk()
    root.title("Secure Utilities - Login")
    root.geometry("900x600")
    root.config(bg=COLORS['light_gray'])
    root.minsize(900, 600)
    
    # Center window
    window_width = 900
    window_height = 600
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