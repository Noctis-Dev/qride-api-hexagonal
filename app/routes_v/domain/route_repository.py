from abc import ABC, abstractmethod
from typing import Optional, List
from app.routes_v.domain.route_model import Route

class RouteRepository: 
    @abstractmethod
    def get (self, route_uuid: str) -> Optional[Route]:
        pass

    def get_all (self, skip: int = 0, limit: int = 100) -> List[Route]:
        pass

    def create (self, route: Route) -> Route:
        pass

    def update (self, route: Route) -> Optional[Route]:
        pass

    def delete (self, route_uui: str) -> bool:
        pass
