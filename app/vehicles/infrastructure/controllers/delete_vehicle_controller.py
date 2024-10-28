from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.delete_vehicle_use_case import DeleteVehicleUseCase
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

class DeleteVehicleController:

    router = APIRouter()

    @router.delete("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def delete_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = DeleteVehicleUseCase(vehicle_repository)
        logging.info(f"Deleting vehicle with uuid: {vehicle_uuid}")
        return use_case.execute(vehicle_uuid)