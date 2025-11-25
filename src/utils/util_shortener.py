# src/utils/util_shortener.py
import hashlib

# Try using pyshorteners if available (faster & real), otherwise fallback to local hash
def shorten_url(long_url: str) -> str:
    long_url = long_url.strip()
    if not long_url:
        return ""
    try:
        import pyshorteners
        s = pyshorteners.Shortener()
        return s.tinyurl.short(long_url)
    except Exception:
        # fallback: deterministic MD5-based short path
        code = hashlib.md5(long_url.encode()).hexdigest()[:8]
        return f"https://short.ly/{code}"
