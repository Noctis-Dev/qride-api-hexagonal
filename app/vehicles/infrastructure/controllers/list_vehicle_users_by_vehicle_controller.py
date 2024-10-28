from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicle_users_by_vehicle_use_case import ListVehicleUsersByVehicleUseCase
from app.vehicles.infrastructure.schemas import VehicleUser
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

class ListVehicleUsersByVehicleController:
    router = APIRouter()

    @router.get("/users/{user_uuid}/vehicles", response_model=list[VehicleUser])
    def read_vehicle_users_by_vehicle(self, vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = ListVehicleUsersByVehicleUseCase(vehicle_repository)
        logging.info(f"Listing users for vehicle with uuid: {vehicle_uuid}")
        return use_case.execute(vehicle_uuid)