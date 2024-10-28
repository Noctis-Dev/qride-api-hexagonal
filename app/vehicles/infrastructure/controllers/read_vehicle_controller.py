from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.read_vehicle_use_case import ReadVehicleUseCase
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

class ReadVehicleController:
    router = APIRouter()

    @router.get("/vehicles/{vehicle_uuid}", response_model=Vehicle)
    def read_vehicle(self, vehicle_uuid: str, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = ReadVehicleUseCase(vehicle_repository)
        vehicle = use_case.execute(vehicle_uuid)
        logging.info(f"Reading vehicle with uuid: {vehicle_uuid}")
        if vehicle is None:
            logging.error(f"Vehicle with uuid {vehicle_uuid} not found")
            raise HTTPException(status_code=404, detail="Vehicle not found")
        return vehicle