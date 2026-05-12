from datetime import datetime

from sqlalchemy import ForeignKey, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Ride(Base):
    __tablename__ = "rides"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    passenger_id: Mapped[int] = mapped_column(ForeignKey("passengers.id"))
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.id"))

    pickup_address: Mapped[str] = mapped_column(String(255))
    destination_address: Mapped[str] = mapped_column(String(255))

    status: Mapped[str] = mapped_column(String(50), default="created")
    price: Mapped[float] = mapped_column(Float, default=0.0)
    distance_km: Mapped[float] = mapped_column(Float, default=0.0)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    passenger = relationship("Passenger", back_populates="rides")
    driver = relationship("Driver", back_populates="rides")
    payment = relationship("Payment", back_populates="ride", uselist=False)