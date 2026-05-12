from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class RideBase(BaseModel):
    pickup_address: str = Field(min_length=3, max_length=255)
    destination_address: str = Field(min_length=3, max_length=255)

    status: str = Field(default="created", max_length=50)

    price: float = Field(ge=0)
    distance_km: float = Field(ge=0)


class RideCreate(RideBase):
    passenger_id: int
    driver_id: int


class RideUpdate(BaseModel):
    pickup_address: str | None = None
    destination_address: str | None = None

    status: str | None = None

    price: float | None = Field(default=None, ge=0)
    distance_km: float | None = Field(default=None, ge=0)


class RideResponse(RideBase):
    id: int

    passenger_id: int
    driver_id: int

    created_at: datetime

    model_config = ConfigDict(from_attributes=True)