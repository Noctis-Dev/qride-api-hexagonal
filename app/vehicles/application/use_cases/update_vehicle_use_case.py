from app.vehicles.domain.repositories import VehicleRepository

class UpdateVehicleUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, user_uuid: str, route_id: int = None, current_location: str = None, status: str = None):
        vehicle = self.vehicle_repository.get(user_uuid)
        if not vehicle:
            raise ValueError(f"Vehicle with id {user_uuid} not found")
        vehicle.update_vehicle(route_id, current_location, status)
        self.vehicle_repository.update(vehicle)