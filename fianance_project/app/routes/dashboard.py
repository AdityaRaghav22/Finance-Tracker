from flask import Blueprint, request, jsonify
from app.service.dashboard_service import Dashboard_Service
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.decorators import role_required

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/")

@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_dashboard():
    user_id = get_jwt_identity()
    dashboard, error = Dashboard_Service.get_dashboard_data(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(dashboard), 200

@dashboard_bp.route("/dashboard/frecord/<type>", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_frecord_by_type(type):
    user_id = get_jwt_identity()
    frecords, error = Dashboard_Service.get_frecord_by_type(type, user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(frecords), 200

@dashboard_bp.route("/dashboard/frecord", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_frecord_by_date():
    user_id = get_jwt_identity()
    date = request.args.get("date")
    frecords, error = Dashboard_Service.get_frecord_by_date(date, user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(frecords), 200

@dashboard_bp.route("/dashboard/category", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_category_wise_data():
    user_id = get_jwt_identity()
    category_wise_data, error = Dashboard_Service.get_category_wise_data(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(category_wise_data), 200

@dashboard_bp.route("/dashboard/monthly", methods=["GET"])
@jwt_required()
@role_required(["admin", "analyst"])
def get_monthly_income_expense_data():
    user_id = get_jwt_identity()
    monthly_data, error = Dashboard_Service.monthly_income_expense_data(user_id)
    if error:
        return jsonify({"message": error}), 400
    return jsonify(monthly_data), 200
