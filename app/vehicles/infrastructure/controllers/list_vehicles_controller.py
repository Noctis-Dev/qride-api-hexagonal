from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.schemas import Vehicle
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicles_use_case import ListVehiclesUseCase
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

class ListVehiclesController:
    router = APIRouter()

    @router.get("/vehicles", response_model=list[Vehicle])
    def read_vehicles(self, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = ListVehiclesUseCase(vehicle_repository)
        logging.info(f"Listing vehicles with skip={skip} and limit={limit}")
        return use_case.execute(skip, limit)