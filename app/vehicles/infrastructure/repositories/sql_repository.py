from typing import List, Optional
import uuid
from sqlalchemy.orm import Session
from app.vehicles.domain.models import Vehicle
from app.vehicles.domain.models import VehicleUser
from app.vehicles.domain.repositories import VehicleRepository
from app.vehicles.infrastructure.models.sql_vehicle_model import SQLVehicle
from app.vehicles.infrastructure.models.sql_vehicle_users_model import VehicleUser as VehicleUserModel
from qride_api_hexagonal.app.users.infrastructure.repositories.sql_repository import UserRepository


class SQLAlchemyVehicleRepository(VehicleRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, vehicle_uuid: str) -> Optional[Vehicle]:
        vehicle = self.db.query(SQLVehicle).filter_by(vehicle_uuid=vehicle_uuid).first()
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
        vehicle_models = self.db.query(SQLVehicle).filter_by(route_id=route_id).all()
        vehicles = [
            Vehicle(
                vehicle_id=vehicle_entity.vehicle_id,
                vehicle_uuid=vehicle_entity.vehicle_uuid,
                route_id=vehicle_entity.route_id,
                current_location=vehicle_entity.current_location,
                status=vehicle_entity.status
            )
            for vehicle_entity in vehicle_models
        ]
        return vehicles
        

    def get_vehicles(self, skip: int = 0, limit: int = 100) -> List[Vehicle]:
        vehicle_models = self.db.query(SQLVehicle).offset(skip).limit(limit).all()
        vehicles = [
            Vehicle(
                vehicle_id=vehicle_entity.vehicle_id,
                vehicle_uuid=vehicle_entity.vehicle_uuid,
                route_id=vehicle_entity.route_id,
                current_location=vehicle_entity.current_location,
                status=vehicle_entity.status
            )
            for vehicle_entity in vehicle_models
        ]
        return vehicles

    def save(self, vehicle: Vehicle) -> Vehicle:
        vehicle_entity = SQLVehicle(
            vehicle_uuid=uuid.uuid4(),
            route_id=vehicle.route_id,
            current_location=vehicle.current_location,
            status=vehicle.status
        )
        self.db.add(vehicle_entity)
        self.db.commit()
        self.db.refresh(vehicle_entity)
        return Vehicle(
            vehicle_id=vehicle_entity.vehicle_id,
            vehicle_uuid=vehicle_entity.vehicle_uuid,
            route_id=vehicle_entity.route_id,
            current_location=vehicle_entity.current_location,
            status=vehicle_entity.status
        )   
    
    def update(self, vehicle: Vehicle) -> None:
        vehicle_entity = self.get(vehicle.vehicle_uuid)
        if vehicle_entity is None:
            raise ValueError(f"Vehicle with UUID {vehicle.vehicle_uuid} not found")
        
        if vehicle.route_id is not None:
            vehicle_entity.route_id = vehicle.route_id
        if vehicle.current_location is not None:
            vehicle_entity.current_location = vehicle.current_location
        if vehicle.status is not None:
            vehicle_entity.status = vehicle.status
        self.db.commit()
        self.db.refresh(vehicle_entity)
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