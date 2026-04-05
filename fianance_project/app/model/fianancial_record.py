from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db
from datetime import datetime

# FinancialRecord
# ----------------
# id
# amount
# type (income / expense)
# category
# date
# notes
# created_by
# created_at


class Frecord(db.Model):
    __tablename__ = "financial_records"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    amount: Mapped[float] = mapped_column(db.Float, nullable=False)
    type: Mapped[str] = mapped_column(db.Enum("income", "expense", name="financial_record_type"), nullable=False, index=True, default="income")
    category: Mapped[str] = mapped_column(db.String(50), nullable=False)
    date: Mapped[datetime] = mapped_column(db.Date, nullable=False)
    notes: Mapped[str] = mapped_column(db.String(255), nullable=True)
    status: Mapped[str] = mapped_column(db.Enum("active", "inactive", name="financial_record_status"), nullable=False, default="active")
    created_by: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", foreign_keys=[created_by], back_populates="financial_records", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "type": self.type,
            "category": self.category,
            "date": self.date,
            "notes": self.notes,
            "status": self.status,
            "created_by": self.created_by,
            "created_at": self.created_at
        }