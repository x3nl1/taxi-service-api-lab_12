from sqlalchemy import ForeignKey, Float, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    ride_id: Mapped[int] = mapped_column(ForeignKey("rides.id"), unique=True)

    amount: Mapped[float] = mapped_column(Float)
    method: Mapped[str] = mapped_column(String(50))  # cash / card
    status: Mapped[str] = mapped_column(String(50), default="pending")

    ride = relationship("Ride", back_populates="payment")