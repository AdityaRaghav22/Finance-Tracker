from app.utils.auth_validators import validate_name, validate_email, validate_password, validate_role, validate_status
from app.model.user import User
from app.extensions import db, bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy import or_

class UserAuth:
    @staticmethod
    def create_user(username, email, password, role):
        if not all([username, email, password, role]) :
            return None, "All fields are required"

        username = username.strip().lower()
        email = email.strip().lower()
        password = password.strip()
        role = role.strip().lower()

        is_valid, error = validate_name(username)
        if not is_valid:
            return None, error

        is_valid, error = validate_email(email)
        if not is_valid:
            return None, error

        is_valid, error = validate_password(password)
        if not is_valid:
            return None, error

        is_valid, error = validate_role(role)
        if not is_valid:
            return None, error
        user = None
        existing_user = User.query.filter(
            or_(User.email == email, User.username == username)
        ).first()

        if existing_user:
            return None, "User already exists"
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(
            username=username,
            email=email,
            password=hashed_password,
            role=role
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user, None

    @staticmethod
    def login_user(password, email= None, username = None):
        if not password:
            return None, "Password is required"
        if not email and not username:
            return None, "Email or username is required"
        if email:
            email = email.strip().lower()
        if username:
            username = username.strip().lower()
        password = password.strip()

        if email:
            is_valid, error = validate_email(email)
            if not is_valid:
                return None, error
        if username:
            is_valid, error = validate_name(username)
            if not is_valid:
                return None, error
        user = None

        print("login in process")
        if email:
            user = db.session.query(User).filter_by(email=email).first()
        elif username:
            user = db.session.query(User).filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user.password, password):
            return None, "Invalid credentials"
        print("user found")
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "role": user.role,
                "username": user.username
            }
        )        
        return access_token, None

    @staticmethod
    def update_user(user_id, username= None, email= None, password= None, role= None, status= None):
        if not user_id:
            return None, "User ID is required"
        user = db.session.get(User, user_id)
        if not user:
            return None, "User not found"
        if username:
            username = username.strip().lower()
            is_valid, error = validate_name(username)
            if not is_valid:
                return None, error
            user.username = username
        if email:
            email = email.strip().lower()
            is_valid, error = validate_email(email)
            if not is_valid:
                return None, error
            user.email = email
        if password:
            password = password.strip()
            is_valid, error = validate_password(password)
            if not is_valid:
                return None, error
            user.password = bcrypt.generate_password_hash(password).decode('utf-8')
        if role:
            role = role.strip().lower()
            is_valid, error = validate_role(role)
            if not is_valid:
                return None, error
            user.role = role
        if status:
            status = status.strip().lower()
            is_valid, error = validate_status(status)
            if not is_valid:
                return None, error
            user.status = status
        db.session.commit()
        return user, None

    @staticmethod
    def delete_user(user_id):
        if not user_id:
            return None, "User ID is required"
        user = db.session.get(User, user_id)
        if not user:
            return None, "User not found"
        user.status = "inactive"
        db.session.commit()
        return user, None

    @staticmethod
    def list_users():
        users = User.query.all()
        if not users:
            return None, "No users found"
        return users, None    
    
    @staticmethod
    def get_user(user_id):
        if not user_id:
            return None, "User ID is required"
        user = db.session.get(User, user_id)
        if not user:
            return None, "User not found"
        return user, None