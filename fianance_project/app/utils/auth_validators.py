def validate_name(username):
    if not username:
        return False, "Username is required"

    username = str(username).strip()

    is_valid, error = ensure_string(username, "username")
    if not is_valid:
        return False, error

    if not username.isalpha():
        return False, "Username is required"

    if len(username) < 3:
        return False, "Username must be at least 3 characters long"
    return True, ""

def validate_email(email):
    is_valid, error = ensure_string(email, "email address")
    if not is_valid:
        return False, error

    if not email:
        return False, "Email required"

    if email.count("@") != 1:
        return False, "Invalid email address"

    username, domain = email.split("@")

    if not username:
        return False, "Invalid email address"

    if "." not in domain:
        return False, "Domain must contain a dot"

    domain_name, extension = domain.rsplit(".", 1)

    if not domain_name or not extension:
        return False, "Invalid domain extension"

    return True, ""

def validate_password(password):
    ensure_string(password, "password")
    if not password:
        return False, "Password is required"

    if len(password) < 8:
        return False, "Password must be at least 6 characters long"
    return True, ""

def validate_role(role):
    ensure_string(role, "role")
    if not role:
        return False, "Role is required"

    if role not in ["admin", "analyst", "viewer"]:
        return False, "Invalid role"
    return True, ""

def validate_status(status):
    ensure_string(status, "status")
    if not status:
        return False, "Status is required"
    if status not in ["active", "inactive"]:
        return False, "Invalid status"
    return True, ""

def ensure_string(value, field):
    if not isinstance(value, str):
        return False, f"Invalid {field}"
    return True, ""