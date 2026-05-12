from pydantic import BaseModel, Field


class PassengerCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=255)
    phone: str = Field(min_length=5, max_length=20)


class PassengerResponse(BaseModel):
    id: int
    full_name: str
    phone: str

    class Config:
        from_attributes = True