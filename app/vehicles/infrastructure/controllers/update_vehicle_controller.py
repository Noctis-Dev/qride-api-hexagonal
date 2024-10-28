from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.schemas import Vehicle, VehicleUpdate
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.update_vehicle_use_case import UpdateVehicleUseCase
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

class UpdateVehicleController:
    router = APIRouter()
    
    #corregir para manejar response 
    @router.put("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def update_vehicle(self, vehicle_uuid: str, vehicle_update: VehicleUpdate, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = UpdateVehicleUseCase(vehicle_repository)
        logging.info(f"Updating vehicle with uuid: {vehicle_uuid}")
        return use_case.execute(
            vehicle_uuid,
            route_id=vehicle_update.route_id,
            current_location=vehicle_update.current_location,
            status=vehicle_update.status
        )