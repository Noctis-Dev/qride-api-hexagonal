from app.vehicles.domain.repositories import VehicleRepository

class ListVehicleUsersByUserUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, user_uuid: str):
        return self.vehicle_repository.get_vehicle_users_by_user(user_uuid)