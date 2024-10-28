from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicles_by_route_use_case import ListVehiclesByRouteUseCase
from app.vehicles.infrastructure.schemas import Vehicle
from app.db import get_db
import logging
import os

# Crear la carpeta de logs si no existe
log_dir = "var/log"
os.makedirs(log_dir, exist_ok=True)

# Configuración básica del logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'myapp.log'), 
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class ListVehicleByRouteController:
    router = APIRouter()
    
    @router.get("/vehicles/route/{route_id}", response_model=list[Vehicle])
    def read_vehicles_by_route(self, route_id: int, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = ListVehiclesByRouteUseCase(vehicle_repository)
        logging.info(f"Listing vehicles for route with id: {route_id}")
        return use_case.execute(route_id)