from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.delete_vehicle_use_case import DeleteVehicleUseCase
from app.vehicles.infrastructure.schemas import Vehicle
from app.db import get_db

class DeleteVehicleController:
    def __init__(self):
        self.use_case = DeleteVehicleUseCase()

    router = APIRouter()

    @router.delete("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def delete_vehicle(self, vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        return self.use_case.execute(vehicle_uuid)