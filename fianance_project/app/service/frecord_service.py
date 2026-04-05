from app.model.fianancial_record import Frecord
from app.utils.frecord_validators import validate_amount, validate_category, validate_date, validate_description, validate_status, validate_type
from app.extensions import db
from app.model.user import User
from datetime import datetime

def serialize_frecord(frecord):
    return {
        "id": frecord.id,
        "amount": frecord.amount,
        "type": frecord.type,
        "category": frecord.category,
        "date": frecord.date,
        "description": frecord.notes,
        "status": frecord.status,
        "created_by": frecord.created_by,
        "created_at": frecord.created_at
    }

class FRecordService:
    @staticmethod
    def create_frecord(user_id, amount, type, category, date, description):
        if user_id is None or amount is None or not all([ type, category, date, description]):
           return None,"All fields are required"

        user = db.session.get(User, user_id)
        if not user:
            return None,"User not found"
        
        amount = float(amount)
        type = type.strip().lower()
        category = category.strip().lower()
        description = description.strip()

        is_valid, error = validate_amount(amount)
        if not is_valid:
            return None, error

        is_valid, error = validate_type(type)
        if not is_valid:
            return None, error

        is_valid, error = validate_category(category)
        if not is_valid:
            return None, error

        is_valid, error = validate_date(date)
        if not is_valid:
            return None, error
        date = datetime.strptime(date, "%d-%m-%Y")

        is_valid, error = validate_description(description)
        if not is_valid:
            return None, error
        
        frecord = Frecord(amount=amount, type=type, category=category, date=date, notes=description, status="active", created_by=user_id)
        db.session.add(frecord)
        db.session.commit()

        return frecord, None

    @staticmethod
    def get_frecord(frecord_id):
        if not frecord_id:
            return None,"Financial record ID is required"

        frecord = db.session.get(Frecord, frecord_id)
        if not frecord:
            return None,"Financial record not found"

        return frecord, None

    @staticmethod
    def update_frecord(frecord_id, amount= None, type= None, category= None, date= None, description= None):
        if not frecord_id:
            return None,"Financial record ID is required"

        frecord = db.session.get(Frecord, frecord_id)
        if not frecord:
            return None,"Financial record not found"

        if amount is not None:
            is_valid, error = validate_amount(amount)
            if not is_valid:
                return None, error
            frecord.amount = amount

        if type:
            type = type.strip().lower()
            is_valid, error = validate_type(type)
            if not is_valid:
                return None, error
            frecord.type = type

        if category:
            category = category.strip().lower()
            is_valid, error = validate_category(category)
            if not is_valid:
                return None, error
            frecord.category = category

        if date:
            is_valid, error = validate_date(date)
            if not is_valid:
                return None, error
            date = datetime.strptime(date, "%d-%m-%Y")
            frecord.date = date

        if description:
            description = description.strip()
            is_valid, error = validate_description(description)
            if not is_valid:
                return None, error
            frecord.notes = description

        db.session.commit()
        return frecord, None

    @staticmethod
    def delete_frecord(frecord_id):
        if not frecord_id:
            return None,"Financial record ID is required"

        frecord = db.session.get(Frecord, frecord_id)
        if not frecord:
            return None,"Financial record not found"

        is_valid, error = validate_status("inactive")
        if not is_valid:
            return None, error

        frecord.status = "inactive"
        db.session.commit()
        return frecord, None

    @staticmethod
    def list_frecords(user_id):
        if not user_id:
            return None,"User ID is required"

        frecords = db.session.query(Frecord).filter(Frecord.created_by == user_id).all()
        return frecords, None
    
    