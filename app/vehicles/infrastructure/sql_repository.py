from typing import List, Optional
import uuid
from sqlalchemy.orm import Session
from app.vehicles.domain.models import Vehicle
from app.vehicles.domain.models import VehicleUser
from app.vehicles.domain.repositories import VehicleRepository
from app.vehicles.infrastructure.sql_vehicle_model import Vehicle as VehicleModel
from app.vehicles.infrastructure.sql_vehicle_users_model import VehicleUser as VehicleUserModel
from app.users.infrastructure.sql_repository import UserRepository


class SQLAlchemyVehicleRepository(VehicleRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, vehicle_uuid: str) -> Optional[Vehicle]:
        vehicle = self.db.query(VehicleModel).filter_by(vehicle_uuid=vehicle_uuid).first()
        if vehicle is None:
            return None
        return Vehicle(
            vehicle_id=vehicle.vehicle_id,
            vehicle_uuid=vehicle.vehicle_uuid,
            route_id=vehicle.route_id,
            current_location=vehicle.current_location,
            status=vehicle.status
        )

    def get_vehicles_by_route(self, route_id: int) -> List[Vehicle]:
        vehicle_models = self.db.query(VehicleModel).filter_by(route_id=route_id).all()
        vehicles = [
            Vehicle(
                vehicle_id=vehicle_model.vehicle_id,
                vehicle_uuid=vehicle_model.vehicle_uuid,
                route_id=vehicle_model.route_id,
                current_location=vehicle_model.current_location,
                status=vehicle_model.status
            )
            for vehicle_model in vehicle_models
        ]
        return vehicles
        

    def get_vehicles(self, skip: int = 0, limit: int = 100) -> List[Vehicle]:
        vehicle_models = self.db.query(VehicleModel).offset(skip).limit(limit).all()
        vehicles = [
            Vehicle(
                vehicle_id=vehicle_model.vehicle_id,
                vehicle_uuid=vehicle_model.vehicle_uuid,
                route_id=vehicle_model.route_id,
                current_location=vehicle_model.current_location,
                status=vehicle_model.status
            )
            for vehicle_model in vehicle_models
        ]
        return vehicles

    def save(self, vehicle: Vehicle) -> Vehicle:
        vehicle_model = VehicleModel(
            vehicle_uuid=uuid.uuid4(),
            route_id=vehicle.route_id,
            current_location=vehicle.current_location,
            status=vehicle.status
        )
        self.db.add(vehicle_model)
        self.db.commit()
        self.db.refresh(vehicle_model)
        return Vehicle(
            vehicle_id=vehicle_model.vehicle_id,
            vehicle_uuid=vehicle_model.vehicle_uuid,
            route_id=vehicle_model.route_id,
            current_location=vehicle_model.current_location,
            status=vehicle_model.status
        )   
    
    def update(self, vehicle: Vehicle) -> None:
        vehicle_model = self.get(vehicle.vehicle_uuid)
        if vehicle_model is None:
            raise ValueError(f"Vehicle with UUID {vehicle.vehicle_uuid} not found")
        
        if vehicle.route_id is not None:
            vehicle_model.route_id = vehicle.route_id
        if vehicle.current_location is not None:
            vehicle_model.current_location = vehicle.current_location
        if vehicle.status is not None:
            vehicle_model.status = vehicle.status
        self.db.commit()
        self.db.refresh(vehicle_model)
        return None
    
    def delete(self, vehicle_uuid: str) -> None:
        db_vehicle = self.get(vehicle_uuid)
        if db_vehicle:
            self.db.delete(db_vehicle)
            self.db.commit()
        return None

    def get_vehicle_users_by_vehicle(self, vehicle_uuid: str) -> List[VehicleUser]:
        db_vehicle = self.get(vehicle_uuid)
        db_vehicle_users = self.db.query(VehicleUserModel).filter(VehicleUserModel.vehicle_id == db_vehicle.vehicle_id).all()
        vehicle_users = [
            VehicleUser(
                vehicle_users_id=db_vehicle_user.vehicle_users_id,
                vehicle_id=db_vehicle_user.vehicle_id,
                user_id=db_vehicle_user.user_id,
                end_date=db_vehicle_user.end_date,
                start_date=db_vehicle_user.start_date,
                is_owner=db_vehicle_user.is_owner
            )
            for db_vehicle_user in db_vehicle_users
        ]
        return vehicle_users
         

    def get_vehicle_users_by_user(self, user_uuid: str) -> List[Vehicle]:
        db_user = UserRepository(self.db).get(user_uuid)
        db_vehicle_users = self.db.query(VehicleUserModel).filter(VehicleUserModel.user_id == db_user.user_id).all()
        vehicle_users = [
            VehicleUser(
                vehicle_users_id=db_vehicle_user.vehicle_users_id,
                vehicle_id=db_vehicle_user.vehicle_id,
                user_id=db_vehicle_user.user_id,
                end_date=db_vehicle_user.end_date,
                start_date=db_vehicle_user.start_date,
                is_owner=db_vehicle_user.is_owner
            )
            for db_vehicle_user in db_vehicle_users
        ]
        return vehicle_users