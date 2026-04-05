from flask import Blueprint

api_v1 = Blueprint("api_v1", __name__,url_prefix = "/")

from app.routes.auth import auth_bp
from app.routes.user import user_bp
from app.routes.frecord import frecord_bp
from app.routes.dashboard import dashboard_bp

api_v1.register_blueprint(auth_bp)
api_v1.register_blueprint(user_bp)
api_v1.register_blueprint(frecord_bp)


api_v1.register_blueprint(dashboard_bp)
