from app.vehicles.domain.repositories import VehicleRepository

class DeleteVehicleUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, vehicle_uuid: str):
        vehicle = self.vehicle_repository.get(vehicle_uuid)
        if not vehicle:
            raise ValueError(f"Vehicle with id {vehicle_uuid} not found")
        self.vehicle_repository.delete(vehicle_uuid)