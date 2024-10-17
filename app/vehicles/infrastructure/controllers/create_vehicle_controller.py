from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.vehicles.infrastructure.repositories.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.use_cases.create_vehicle_use_case import CreateVehicleUseCase
from app.vehicles.infrastructure.schemas import VehicleCreate, Vehicle
from app.db import get_db

class CreateVehicleController:
    def __init__(self):
        self.use_case = CreateVehicleUseCase()
    
    router = APIRouter()

    @router.post("/vehicles", response_model=Vehicle)
    def create_vehicle(self, vehicle_create: VehicleCreate, db: Session = Depends(get_db)):
        vehicle_repository = SQLAlchemyVehicleRepository(db)
        self.use_case(vehicle_repository)
        try:
            new_vehicle = self.use_case.execute(
                route_id=vehicle_create.route_id,
                current_location=vehicle_create.current_location,
                status=vehicle_create.status
            )
            return new_vehicle
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Invalid vehicle status or other integrity constraint violation")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))