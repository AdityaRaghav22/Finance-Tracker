from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from datetime import datetime

# User
# ----
# id
# username
# email
# password
# role
# status
# created_at

class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False)
    email: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    role: Mapped[str] = mapped_column(db.Enum("viewer", "analyst", "admin", name="user_roles"), nullable=False, index=True, default="viewer")
    status: Mapped[str] = mapped_column(db.Enum("active", "inactive", name="user_status"), nullable=False, index=True, default="active")
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow)
    
    financial_records: Mapped[list["Frecord"]] = relationship("Frecord", foreign_keys="[Frecord.created_by]", back_populates="user", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "status": self.status,
            "created_at": self.created_at,
        }