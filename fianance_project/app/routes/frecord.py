from flask import Blueprint, request, jsonify
from app.service.frecord_service import FRecordService
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.decorators import role_required

frecord_bp = Blueprint("frecord", __name__, url_prefix="/")

@frecord_bp.route("/frecord", methods=["POST"])
@jwt_required()
@role_required(["admin", "viewer"])
def create_frecord():
    data = request.get_json()

    if not data:
        return jsonify({"message": "Data is required"}), 400

    user_id = get_jwt_identity()
    amount = data.get("amount")
    type = data.get("type")
    category = data.get("category")
    date = data.get("date")
    description = data.get("description")
    frecord, error = FRecordService.create_frecord(user_id=user_id, amount=amount, type=type, category=category, date=date, description=description)

    if error:
        return jsonify({"message": error}), 400

    return jsonify({"message": "Financial record created successfully"}), 200

@frecord_bp.route("/frecord/<int:f_id>", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_frecord(f_id):
    frecord, error = FRecordService.get_frecord(f_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(frecord.to_dict()), 200

@frecord_bp.route("/frecord/<int:f_id>", methods=["PUT"])
@jwt_required()
@role_required(["admin", "viewer"])
def update_frecord(f_id):
    data = request.get_json()
    if not data:
        return jsonify({"message": "Data is required"}), 400

    user_id = get_jwt_identity()
    amount = data.get("amount")
    type = data.get("type")
    category = data.get("category")
    date = data.get("date")
    description = data.get("description")
    frecord, error = FRecordService.update_frecord(frecord_id=f_id, amount=amount, type=type, category=category, date=date, description=description)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(frecord.to_dict()), 200

@frecord_bp.route("/frecord/<int:f_id>", methods=["DELETE"])
@jwt_required()
@role_required("admin")
def delete_frecord(f_id):
    frecord, error = FRecordService.delete_frecord(f_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify({"message": "Financial record deleted successfully"}), 200

@frecord_bp.route("/frecord", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def list_frecords():
    user_id = request.args.get("user_id")
    frecords, error = FRecordService.list_frecords(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify([frecord.to_dict() for frecord in frecords]), 200
