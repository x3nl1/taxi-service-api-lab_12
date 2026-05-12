from fastapi import FastAPI

from app.routers.health import router as health_router
from app.api.passenger import router as passenger_router
from app.api.driver import router as driver_router

app = FastAPI(
    title="Taxi Service API",
    description="REST API for taxi service management",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(passenger_router)
app.include_router(driver_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Taxi Service API is running"}