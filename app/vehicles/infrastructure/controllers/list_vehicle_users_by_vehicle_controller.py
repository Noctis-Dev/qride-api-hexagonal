from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicle_users_by_vehicle_use_case import ListVehicleUsersByVehicleUseCase
from app.vehicles.infrastructure.schemas import VehicleUser
from app.db import get_db

class ListVehicleUsersByVehicleController:
    router = APIRouter()

    def __init__(self):
        self.use_case = ListVehicleUsersByVehicleUseCase()

    @router.get("/users/{user_uuid}/vehicles", response_model=list[VehicleUser])
    def read_vehicle_users_by_vehicle(self, vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        return self.use_case.execute(vehicle_uuid)