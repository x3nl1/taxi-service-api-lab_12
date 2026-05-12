from fastapi import FastAPI

app = FastAPI(
    title="Taxi Service API",
    description="REST API for taxi service management",
    version="1.0.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Taxi Service API is running"}