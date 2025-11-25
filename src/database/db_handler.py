import sqlite3
import os
from contextlib import contextmanager

# Use absolute path for database
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(DB_DIR, "users.db")

@contextmanager
def get_db_connection():
    """Context manager for safe database connections"""
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME, timeout=10.0)
        conn.execute("PRAGMA journal_mode=WAL")  # Enable Write-Ahead Logging
        conn.execute("PRAGMA busy_timeout=5000")  # 5 second busy timeout
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()

def init_db():
    """Initialize the database with users table"""
    try:
        with get_db_connection() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            # Create index for faster username lookups
            cur.execute("""
                CREATE INDEX IF NOT EXISTS idx_username 
                ON users(username)
            """)
            conn.commit()
            print(f"Database initialized at: {DB_NAME}")
    except Exception as e:
        print(f"Database initialization error: {e}")
        raise