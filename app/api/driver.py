from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.driver import DriverCreate, DriverResponse
from app.crud import driver as crud

router = APIRouter(prefix="/drivers", tags=["Drivers"])


@router.post("/", response_model=DriverResponse)
def create(data: DriverCreate, db: Session = Depends(get_db)):
    return crud.create_driver(db, data)


@router.get("/", response_model=list[DriverResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_drivers(db)


@router.get("/{driver_id}", response_model=DriverResponse)
def read_one(driver_id: int, db: Session = Depends(get_db)):
    return crud.get_driver(db, driver_id)


@router.put("/{driver_id}", response_model=DriverResponse)
def update(driver_id: int, data: DriverCreate, db: Session = Depends(get_db)):
    return crud.update_driver(db, driver_id, data)


@router.delete("/{driver_id}")
def delete(driver_id: int, db: Session = Depends(get_db)):
    return crud.delete_driver(db, driver_id)