from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.schemas import Vehicle, VehicleUpdate
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.update_vehicle_use_case import UpdateVehicleUseCase
from app.db import get_db


class UpdateVehicleController:
    router = APIRouter()

    def __init__(self):
        self.use_case = UpdateVehicleUseCase()
    
    #corregir para manejar response 
    @router.put("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def update_vehicle(self, vehicle_uuid: str, vehicle_update: VehicleUpdate, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        return self.use_case.execute(
            vehicle_uuid,
            route_id=vehicle_update.route_id,
            current_location=vehicle_update.current_location,
            status=vehicle_update.status
        )