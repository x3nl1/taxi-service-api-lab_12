from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255))
    license_number: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)

    rides = relationship("Ride", back_populates="driver")