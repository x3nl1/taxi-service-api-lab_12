from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.passenger import PassengerCreate, PassengerResponse
from app.crud import passenger as crud

router = APIRouter(prefix="/passengers", tags=["Passengers"])


@router.post("/", response_model=PassengerResponse)
def create(data: PassengerCreate, db: Session = Depends(get_db)):
    return crud.create_passenger(db, data)


@router.get("/", response_model=list[PassengerResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_passengers(db)


@router.get("/{passenger_id}", response_model=PassengerResponse)
def read_one(passenger_id: int, db: Session = Depends(get_db)):
    return crud.get_passenger(db, passenger_id)


@router.put("/{passenger_id}", response_model=PassengerResponse)
def update(passenger_id: int, data: PassengerCreate, db: Session = Depends(get_db)):
    return crud.update_passenger(db, passenger_id, data)


@router.delete("/{passenger_id}")
def delete(passenger_id: int, db: Session = Depends(get_db)):
    return crud.delete_passenger(db, passenger_id)