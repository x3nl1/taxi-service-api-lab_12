from sqlalchemy.orm import Session

from app.models.ride import Ride
from app.schemas.ride import RideCreate, RideUpdate


def create_ride(db: Session, ride_data: RideCreate) -> Ride:
    ride = Ride(**ride_data.model_dump())

    db.add(ride)
    db.commit()
    db.refresh(ride)

    return ride


def get_rides(db: Session) -> list[Ride]:
    return db.query(Ride).all()


def get_ride_by_id(db: Session, ride_id: int) -> Ride | None:
    return db.query(Ride).filter(Ride.id == ride_id).first()


def update_ride(
    db: Session,
    ride_id: int,
    ride_data: RideUpdate,
) -> Ride | None:
    ride = get_ride_by_id(db, ride_id)

    if not ride:
        return None

    update_data = ride_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(ride, key, value)

    db.commit()
    db.refresh(ride)

    return ride


def delete_ride(db: Session, ride_id: int) -> bool:
    ride = get_ride_by_id(db, ride_id)

    if not ride:
        return False

    db.delete(ride)
    db.commit()

    return True