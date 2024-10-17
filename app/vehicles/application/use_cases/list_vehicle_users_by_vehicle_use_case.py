from app.vehicles.domain.repositories import VehicleRepository

class ListVehicleUsersByVehicleUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, vehicle_uuid: str):
        return self.vehicle_repository.get_vehicle_users_by_vehicle(vehicle_uuid)