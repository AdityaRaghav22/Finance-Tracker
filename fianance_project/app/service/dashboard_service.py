from app.model.fianancial_record import Frecord
from app.utils.frecord_validators import validate_type, validate_category, validate_date
from app.service.frecord_service import serialize_frecord
from sqlalchemy import func, extract
from app.extensions import db

class Dashboard_Service:    
    @staticmethod
    def get_dashboard_data(user_id):
        data = {}

        if not user_id:
            return None, "User ID is required"
            
        data["total_income"] = db.session.query(func.sum(Frecord.amount)).filter(
            Frecord.created_by == user_id,
            Frecord.type == "income"
        ).scalar() or 0

        data["total_expense"] = db.session.query(func.sum(Frecord.amount)).filter(
            Frecord.created_by == user_id,
            Frecord.type == "expense"
        ).scalar() or 0

        data["balance"] = data["total_income"] - data["total_expense"]

        return data, None

    @staticmethod
    def get_frecord_by_type(type, user_id):
        if not type:
            return None, "Type is required"

        is_valid, error = validate_type(type)
        if not is_valid:
            return None, error

        if not user_id:
            return None, "User ID is required" 

        frecords = db.session.query(Frecord).filter(Frecord.type == type, Frecord.created_by == user_id).all()
        return [serialize_frecord(frecord) for frecord in frecords], None

    @staticmethod
    def get_frecord_by_date(date, user_id):
        if not date:
            return None, "Date is required"

        date = date.strip()

        is_valid, error = validate_date(date)
        if not is_valid:
            return None, error

        if not user_id:
            return None, "User ID is required" 

        frecords = db.session.query(Frecord).filter(Frecord.date == date, Frecord.created_by == user_id).all()
        return [serialize_frecord(frecord) for frecord in frecords], None

    @staticmethod
    def get_category_wise_data(user_id):
        if not user_id:
            return None, "User ID is required"

        frecords = db.session.query(Frecord).filter(Frecord.created_by == user_id).all()
        category_wise_data = {}

        for frecord in frecords:
            if frecord.category not in category_wise_data:
                category_wise_data[frecord.category] = []

            category_wise_data[frecord.category].append(serialize_frecord(frecord))
        return category_wise_data, None

    @staticmethod
    def monthly_income_expense_data(user_id):

        if not user_id:
            return None, "User ID is required"

        results = db.session.query(
            extract("month", Frecord.date).label("month"),
            Frecord.type,
            func.sum(Frecord.amount)
        ).filter(
            Frecord.created_by == user_id
        ).group_by(
            extract("month", Frecord.date),
            Frecord.type
        ).all()

        balance = db.session.query(func.sum(Frecord.amount)).filter(
            Frecord.created_by == user_id,
            Frecord.type == "income"
        ).scalar() or 0 - db.session.query(func.sum(Frecord.amount)).filter(
            Frecord.created_by == user_id,
            Frecord.type == "expense"
        ).scalar() or 0

        monthly_data = {}

        for month, type, total in results:
            month_key = str(int(month)) # Ensure it's a standard string for JSON

            if month_key not in monthly_data:
                monthly_data[month_key] = {"income": 0, "expense": 0}

            monthly_data[month_key][type] = float(total)
            monthly_data[month_key]["balance"] = monthly_data[month_key]["income"] - monthly_data[month_key]["expense"]

        return monthly_data, None