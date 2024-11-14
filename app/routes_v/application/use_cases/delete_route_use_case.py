from app.routes_v.domain.route_repository import RouteRepository

class DeleteRouteUseCase:
    def __init__(self, route_repository: RouteRepository) -> None:
        self.route_repository=route_repository
        pass

    def execute(self, route_uuid: str):
        route = self.route_repository.get(route_uuid)
        if route:
            self.route_repository.delete(route)
            return True
        return False