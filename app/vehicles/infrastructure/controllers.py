from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.vehicles.infrastructure.sql_repository import SQLAlchemyVehicleRepository
from app.vehicles.application.services import VehicleService
from app.vehicles.infrastructure.schemas import VehicleCreate, VehicleUpdate, Vehicle, VehicleUser
from app.db import get_db

router = APIRouter()

@router.get("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def read_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    vehicle = vehicle_service.get_vehicle(vehicle_uuid)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

@router.get("/vehicles/", response_model=list[Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.get_vehicles(skip, limit)

@router.get("/vehicles/route/{route_id}", response_model=list[Vehicle])
def read_vehicles_by_route(route_id: int, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.get_vehicles_by_route(route_id)

@router.post("/vehicles", response_model=Vehicle)
def create_vehicle(vehicle_create: VehicleCreate, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    try:
        new_vehicle = vehicle_service.create_vehicle(
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

#corregir para manejar response 
@router.put("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def update_vehicle(vehicle_uuid: str, vehicle_update: VehicleUpdate, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.update_vehicle(
        vehicle_uuid,
        route_id=vehicle_update.route_id,
        current_location=vehicle_update.current_location,
        status=vehicle_update.status
    )

#corregir para manejar response
@router.delete("/vehicles/{vehicle_uuid}", response_model=Vehicle)
def delete_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.delete_vehicle(vehicle_uuid)

@router.get("/vehicles/{vehicle_uuid}/users", response_model=list[VehicleUser])
def read_vehicle_users_by_vehicle(vehicle_uuid: str, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.get_vehicle_users_by_vehicle(vehicle_uuid)

@router.get("/users/{user_uuid}/vehicles", response_model=list[VehicleUser])
def read_vehicle_users_by_user(user_uuid: int, db: Session = Depends(get_db)):
    vehicle_repository = SQLAlchemyVehicleRepository(db)
    vehicle_service = VehicleService(vehicle_repository)
    return vehicle_service.get_vehicle_users_by_user(user_uuid)