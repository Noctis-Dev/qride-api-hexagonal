from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.schemas import Vehicle
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicles_use_case import ListVehiclesUseCase
from app.db import get_db

class ListVehiclesController:
    router = APIRouter()

    def __init__(self):
        self.use_case = ListVehiclesUseCase()

    @router.get("/vehicles", response_model=list[Vehicle])
    def read_vehicles(self, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        return self.use_case.execute(skip, limit)