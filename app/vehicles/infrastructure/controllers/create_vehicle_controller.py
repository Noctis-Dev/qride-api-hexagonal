from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.create_vehicle_use_case import CreateVehicleUseCase
from app.vehicles.infrastructure.schemas import VehicleCreate, Vehicle
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

class CreateVehicleController:
    
    router = APIRouter()

    @router.post("/vehicles", response_model=Vehicle)
    def create_vehicle(vehicle_create: VehicleCreate, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = CreateVehicleUseCase(vehicle_repository)
        try:
            new_vehicle = use_case.execute(
                route_id=vehicle_create.route_id,
                current_location=vehicle_create.current_location,
                status=vehicle_create.status
            )
            logging.info(f"Vehicle created: {new_vehicle}")
            return new_vehicle
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Invalid vehicle status or other integrity constraint violation")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))