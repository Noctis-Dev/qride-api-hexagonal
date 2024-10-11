from abc import ABC, abstractmethod
from typing import Optional, List
from app.vehicles.domain.models import Vehicle, VehicleUser

class VehicleRepository(ABC):
    @abstractmethod
    def get(self, vehicle_uuid: str) -> Optional[Vehicle]:
        pass

    @abstractmethod
    def get_vehicles_by_route(self, route_id: int) -> List[Vehicle]:
        pass

    @abstractmethod
    def get_vehicles(self, skip: int = 0, limit: int = 100) -> List[Vehicle]:
        pass

    @abstractmethod
    def save(self, vehicle: Vehicle) -> Vehicle:
        pass

    @abstractmethod
    def update(self, vehicle: Vehicle) -> None:
        pass

    @abstractmethod
    def delete(self, vehicle_uuid: str) -> None:
        pass

    @abstractmethod
    def get_vehicle_users_by_vehicle(self, vehicle_uuid: str) -> List[VehicleUser]:
        pass

    @abstractmethod
    def get_vehicle_users_by_user(self, user_uuid: str) -> List[Vehicle]:
        pass