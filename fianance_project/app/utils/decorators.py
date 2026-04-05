from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt
from flask import jsonify


def role_required(required_role):
    """Allow access only if user's role matches."""
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            user_role = claims.get("role")

            if user_role not in required_role:
                return jsonify({"msg": "Forbidden: Insufficient permissions"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator


def admin_required(fn):
    """Shortcut decorator for admin access."""
    return role_required("admin")(fn)