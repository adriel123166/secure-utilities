# src/auth/register.py
import sqlite3
from tkinter import messagebox
from src.utils.password import hash_password
from src.database.db_handler import DB_NAME

def register_user(username: str, password: str) -> bool:
    """
    Create a new user. Returns True on success, False on failure.
    Uses messageboxes for user feedback from GUI.
    """
    username = (username or "").strip()
    password = (password or "").strip()
    if not username or not password:
        messagebox.showwarning("Missing", "Please enter both username and password.")
        return False

    hashed, salt = hash_password(password)
    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)",
            (username, hashed, salt)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Account created successfully.")
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
        return False
    except Exception as e:
        messagebox.showerror("Error", f"DB error: {e}")
        return False
