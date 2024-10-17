from app.vehicles.domain.repositories import VehicleRepository

class ListVehiclesByRouteUseCase:
    def __init__ (self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def execute(self, route_id: int):
        return self.vehicle_repository.get_vehicles_by_route(route_id)