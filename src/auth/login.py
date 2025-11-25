# src/auth/login.py
import sqlite3
from src.utils.password import hash_password
from src.database.db_handler import DB_NAME

def login_user(username: str, password: str) -> bool:
    username = (username or "").strip()
    password = (password or "").strip()
    if not username or not password:
        return False

    try:
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        conn.close()
        if not row:
            return False
        stored_hash, salt = row
        entered_hash, _ = hash_password(password, salt)
        return stored_hash == entered_hash
    except Exception:
        return False
