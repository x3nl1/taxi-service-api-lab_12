from pydantic import BaseModel, Field


class DriverCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=255)
    license_number: str = Field(min_length=3, max_length=50)


class DriverResponse(BaseModel):
    id: int
    full_name: str
    license_number: str
    is_available: bool

    class Config:
        from_attributes = True