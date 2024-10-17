from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from qride_api_hexagonal.app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicles_by_route_use_case import ListVehiclesByRouteUseCase
from app.vehicles.infrastructure.schemas import Vehicle
from app.db import get_db

class ListVehicleByRouteController:
    router = APIRouter()

    def __init__(self):
        self.use_case = ListVehiclesByRouteUseCase()
    
    @router.get("/vehicles/route/{route_id}", response_model=list[Vehicle])
    def read_vehicles_by_route(self, route_id: int, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        return self.use_case.execute(route_id)