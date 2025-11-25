# src/utils/password.py
import hashlib
import os

def hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
    """
    Return (hash, salt). If salt is None, a new salt is generated.
    """
    if salt is None:
        salt = os.urandom(16).hex()
    h = hashlib.sha256((password + salt).encode()).hexdigest()
    return h, salt
