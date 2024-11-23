from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password: str) -> str:
    """Generate a hashed password."""
    return generate_password_hash(password)

def verify_password(hashed_password: str, password: str) -> bool:
    """Verify a password against a hashed one."""
    return check_password_hash(hashed_password, password)
