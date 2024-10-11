import datetime


class Vehicle:
    def __init__(self, vehicle_id: int, vehicle_uuid: str, route_id: int, current_location: str, status: str):
        self.vehicle_id = vehicle_id
        self.vehicle_uuid = vehicle_uuid
        self.route_id = route_id
        self.current_location = current_location
        self.status = status

    @staticmethod
    def create_new_vehicle(route_id: int, current_location: str, status: str):
        return Vehicle( vehicle_id= None,vehicle_uuid=None ,route_id= route_id, current_location= current_location, status= status)
    
    def update_vehicle(self, route_id: int = None, current_location: str = None, status: str = None):
        if route_id is not None:
            self.route_id = route_id
        if current_location is not None:
            self.current_location = current_location
        if status is not None:
            self.status = status

class VehicleUser:
    def __init__(self, vehicle_users_id: int, vehicle_id: int, user_id: int, start_date: datetime, end_date: datetime, is_owner: bool):
        self.vehicle_users_id = vehicle_users_id
        self.vehicle_id = vehicle_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.is_owner = is_owner

    @staticmethod
    def create_new_vehicle_user(vehicle_id: int, user_id: int, start_date: datetime, end_date: datetime, is_owner: bool):
        return VehicleUser(vehicle_users_id=None, vehicle_id=vehicle_id, user_id=user_id, start_date=start_date, end_date=end_date, is_owner=is_owner)