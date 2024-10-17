from app.vehicles.domain.repositories import VehicleRepository

class ListVehiclesUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, skip: int = 0, limit: int = 100):
        return self.vehicle_repository.get_vehicles(skip, limit)