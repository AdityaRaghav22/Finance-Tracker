from app.utils.auth_validators import ensure_string
from datetime import datetime

def validate_amount(amount):
    if not amount:
        return False, "Amount is required"
    if not isinstance(amount, (int, float)) or amount <= 0:
        return False, "Amount must be a positive number"
    return True, ""

def validate_type(type):
    if not type:
        return False, "Type is required"
    is_valid, error = ensure_string(type, "type")
    if not is_valid:
        return False, error
    if type not in ["income", "expense"]:
        return False, "Invalid type"
    return True, ""

def validate_category(category):
    if not category:
        return False, "Category is required"
    is_valid, error = ensure_string(category, "category")
    if not is_valid:
        return False, error
    return True, ""

def validate_date(date_str):
    if not date_str:
        return False, "Date is required"
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        return False, "Invalid date format"
    return True, ""

def validate_description(description):
    if not description:
        return False, "Description is required"
    is_valid, error = ensure_string(description, "description")
    if not is_valid:
        return False, error

    if len(description) > 500:
        return False, "Description too long"

    return True, ""

def validate_status(status):
    if not status:
        return False, "Status is required"
    is_valid, error = ensure_string(status, "status")
    if not is_valid:
        return False, error
    if status not in ["active", "inactive"]:
        return False, "Invalid status"
    return True, ""