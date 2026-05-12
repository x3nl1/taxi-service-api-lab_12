from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.ride import (
    create_ride,
    delete_ride,
    get_ride_by_id,
    get_rides,
    update_ride,
)
from app.dependencies import get_db
from app.schemas.ride import RideCreate, RideResponse, RideUpdate

router = APIRouter(
    prefix="/rides",
    tags=["Rides"],
)


@router.post(
    "/",
    response_model=RideResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_new_ride(
    ride: RideCreate,
    db: Session = Depends(get_db),
) -> RideResponse:
    return create_ride(db, ride)


@router.get(
    "/",
    response_model=list[RideResponse],
)
def get_all_rides(
    db: Session = Depends(get_db),
) -> list[RideResponse]:
    return get_rides(db)


@router.get(
    "/{ride_id}",
    response_model=RideResponse,
)
def get_ride(
    ride_id: int,
    db: Session = Depends(get_db),
) -> RideResponse:
    ride = get_ride_by_id(db, ride_id)

    if not ride:
        raise HTTPException(
            status_code=404,
            detail="Ride not found",
        )

    return ride


@router.put(
    "/{ride_id}",
    response_model=RideResponse,
)
def update_existing_ride(
    ride_id: int,
    ride_data: RideUpdate,
    db: Session = Depends(get_db),
) -> RideResponse:
    updated_ride = update_ride(
        db,
        ride_id,
        ride_data,
    )

    if not updated_ride:
        raise HTTPException(
            status_code=404,
            detail="Ride not found",
        )

    return updated_ride


@router.delete("/{ride_id}")
def delete_existing_ride(
    ride_id: int,
    db: Session = Depends(get_db),
) -> dict[str, str]:
    deleted = delete_ride(db, ride_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Ride not found",
        )

    return {"message": "Ride deleted successfully"}