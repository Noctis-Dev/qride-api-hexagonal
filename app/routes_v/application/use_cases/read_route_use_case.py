from app.routes_v.domain.route_repository import RouteRepository

class ReadRoutesUseCase:
    def __init__(self, route_repository: RouteRepository) -> None:
        self.rouetes_repository = route_repository
        pass

    def execute(self, route_uuid: str):
        return self.rouetes_repository.get(route_uuid)