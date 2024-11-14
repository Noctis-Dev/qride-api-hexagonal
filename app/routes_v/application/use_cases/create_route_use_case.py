from app.routes_v.domain.route_model import Route
from app.routes_v.domain.route_repository import RouteRepository

class CreateRouteUseCase:
    def __init__(self, route_repository: RouteRepository, ) -> None:
        self.route_repository = route_repository
        pass

    def execute(self, route_id: int, route_type: str, name: str, description: str, start_location: bool, end_location: bool, waypoints: bool, distance: float, estimated_duration: bool, created_at: str, updated_at: str):
        
        if self.route_repository.get(route_id):
            raise ValueError(f"La ruta que intenta subir ya existe, intente actualisarla en su defecto.")
        
        new_route = Route.create_new_route(route_id=route_id,
                                           route_type=route_type,
                                           name=name,
                                           description=description,
                                           start_location=start_location,
                                           end_location=end_location,
                                           waypoints=waypoints,
                                           distance=distance,
                                           estimated_duration=estimated_duration,
                                           created_at=created_at,
                                           updated_at=updated_at)
        
        return self.route_repository.save(new_route)