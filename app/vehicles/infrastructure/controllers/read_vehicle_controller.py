from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.read_vehicle_use_case import ReadVehicleUseCase
from app.vehicles.infrastructure.schemas import Vehicle
from app.db import get_db

class ReadVehicleController:
    router = APIRouter()

    def __init__(self):
        self.use_case = ReadVehicleUseCase()

    @router.get("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def read_vehicle(self, vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        vehicle = self.use_case.execute(vehicle_uuid)
        if vehicle is None:
            raise HTTPException(status_code=404, detail="Vehicle not found")
        return vehicle