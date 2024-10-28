from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.list_vehicle_users_by_user_use_case import ListVehicleUsersByUserUseCase
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

class ListVehicleUsersByUserController:

    router = APIRouter()

    @router.get("/users/{user_uuid}/vehicles", response_model=list[VehicleUser])
    def read_vehicle_users_by_user(user_uuid: int, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        use_case = ListVehicleUsersByUserUseCase(vehicle_repository)
        logging.info(f"Listing vehicles for user with uuid: {user_uuid}")
        return use_case.execute(user_uuid)