from app.vehicles.domain.models import Vehicle
from app.vehicles.domain.repositories import VehicleRepository

class VehicleService:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def get_vehicle(self, vehicle_uuid: str):
        return self.vehicle_repository.get(vehicle_uuid)
    
    def get_vehicles_by_route(self, route_id: int):
        return self.vehicle_repository.get_vehicles_by_route(route_id)
    
    def get_vehicles(self, skip: int = 0, limit: int = 100):
        return self.vehicle_repository.get_vehicles(skip, limit)
    
    def create_vehicle(self, route_id: int, current_location: str, status: str):
        new_vehicle = Vehicle.create_new_vehicle(route_id=route_id, current_location=current_location, status=status)
        return self.vehicle_repository.save(new_vehicle)
    
    def update_vehicle(self, user_uuid: str, route_id: int = None, current_location: str = None, status: str = None):
        vehicle = self.vehicle_repository.get(user_uuid)
        if not vehicle:
            raise ValueError(f"Vehicle with id {user_uuid} not found")
        vehicle.update_vehicle(route_id, current_location, status)
        self.vehicle_repository.update(vehicle)
    
    def delete_vehicle(self, vehicle_uuid: str):
        vehicle = self.vehicle_repository.get(vehicle_uuid)
        if not vehicle:
            raise ValueError(f"Vehicle with id {vehicle_uuid} not found")
        self.vehicle_repository.delete(vehicle_uuid)
    
    def get_vehicle_users_by_vehicle(self, vehicle_uuid: str):
        return self.vehicle_repository.get_vehicle_users_by_vehicle(vehicle_uuid)
    
    def get_vehicle_users_by_user(self, user_uuid: str):
        return self.vehicle_repository.get_vehicle_users_by_user(user_uuid)