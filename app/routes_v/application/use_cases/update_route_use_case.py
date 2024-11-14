from app.routes_v.domain.route_repository import RouteRepository

class UpdateRouteUseCase:
    def __init__(self, route_ropository: RouteRepository) -> None:
        self.route_repository = route_ropository
        pass

    def execute(self, route_uuid:str = None, name: str = None, description= None, start_location=None, end_location=None, waypoints=None, dsitance=None, estimated_duration, update_at=None):