from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.passenger import Passenger
from app.schemas.passenger import PassengerCreate


def create_passenger(db: Session, data: PassengerCreate):
    passenger = Passenger(**data.model_dump())
    db.add(passenger)
    db.commit()
    db.refresh(passenger)
    return passenger


def get_passengers(db: Session):
    return db.query(Passenger).all()


def get_passenger(db: Session, passenger_id: int):
    passenger = db.query(Passenger).filter(Passenger.id == passenger_id).first()
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    return passenger


def update_passenger(db: Session, passenger_id: int, data: PassengerCreate):
    passenger = get_passenger(db, passenger_id)

    passenger.full_name = data.full_name
    passenger.phone = data.phone

    db.commit()
    db.refresh(passenger)
    return passenger


def delete_passenger(db: Session, passenger_id: int):
    passenger = get_passenger(db, passenger_id)
    db.delete(passenger)
    db.commit()
    return {"message": "deleted"}