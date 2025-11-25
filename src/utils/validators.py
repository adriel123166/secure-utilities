def validate_username(username):
    if not username or len(username) < 3:
        return False, "Username must be at least 3 characters long."
    return True, ""

def validate_password(password):
    if not password or len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""

def validate_registration(username, password):
    is_valid_username, username_message = validate_username(username)
    is_valid_password, password_message = validate_password(password)

    if not is_valid_username:
        return False, username_message
    if not is_valid_password:
        return False, password_message

    return True, "Validation successful."

def validate_login(username, password):
    if not username:
        return False, "Username cannot be empty."
    if not password:
        return False, "Password cannot be empty."
    
    return True, "Validation successful."