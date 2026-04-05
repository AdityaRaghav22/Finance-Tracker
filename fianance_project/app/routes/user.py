from flask import Blueprint, request, jsonify
from app.service.auth_service import UserAuth
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.decorators import role_required

user_bp = Blueprint("users", __name__, url_prefix="/")

@user_bp.route("/user/<int:user_id>", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_user(user_id):
    user, error = UserAuth.get_user(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(user.to_dict()), 200

@user_bp.route("/user", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def list_users():
    users, error = UserAuth.list_users()
    if error:
        return jsonify({"message": error}), 400
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route("/user/<int:user_id>", methods=["PUT"])
@jwt_required()
@role_required("admin")
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Data is required"}), 400
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    status = data.get("status")

    user, error = UserAuth.update_user(user_id, username, email, password, role, status)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(user.to_dict()), 200

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_user(user_id):
    user, error = UserAuth.delete_user(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "User deleted successfully"}), 200
