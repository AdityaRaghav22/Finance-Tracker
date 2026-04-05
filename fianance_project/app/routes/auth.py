from flask import Blueprint, request, jsonify

from app.service.auth_service import UserAuth

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return {"message": "Data is required"}, 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not username or not email or not password or not role:
        return {"message": "All fields are required"}, 400

    user, error = UserAuth.create_user(username, email, password, role)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "User created successfully"}), 200

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return {"message": "Data is required"}, 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username and not email:
        return {"message": "Username or email is required"}, 400
    if not password:
        return {"message": "Password is required"}, 400

    token, error = UserAuth.login_user(password, email, username)
    if error:
        print("route failed")
        return jsonify({"message": error}), 400
    return jsonify({"access_token": token}), 200
