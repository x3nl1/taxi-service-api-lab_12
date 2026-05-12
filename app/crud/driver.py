from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.driver import Driver
from app.schemas.driver import DriverCreate


def create_driver(db: Session, data: DriverCreate):
    driver = Driver(
        full_name=data.full_name,
        license_number=data.license_number,
        is_available=True,
    )
    db.add(driver)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="License number must be unique")

    db.refresh(driver)
    return driver


def get_drivers(db: Session):
    return db.query(Driver).all()


def get_driver(db: Session, driver_id: int):
    driver = db.query(Driver).filter(Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


def update_driver(db: Session, driver_id: int, data: DriverCreate):
    driver = get_driver(db, driver_id)

    driver.full_name = data.full_name
    driver.license_number = data.license_number

    db.commit()
    db.refresh(driver)
    return driver


def delete_driver(db: Session, driver_id: int):
    driver = get_driver(db, driver_id)
    db.delete(driver)
    db.commit()
    return {"message": "deleted"}