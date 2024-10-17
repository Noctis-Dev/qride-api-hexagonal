from app.vehicles.domain.models import Vehicle
from app.vehicles.domain.repositories import VehicleRepository

class CreateVehicleUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, route_id: int, current_location: str, status: str):
        new_vehicle = Vehicle.create_new_vehicle(route_id=route_id, current_location=current_location, status=status)
        return self.vehicle_repository.save(new_vehicle)