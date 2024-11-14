class Route:

    def __init__(self,route_id, route_uuid, name, description=None, start_location=None, end_location=None, waypoints=None, distance=0.0, estimated_duration=0, created_at=None, updated_at=None):
        
        self.route_id = route_id
        self.route_uuid = route_uuid
        self.name = name
        self.description = description
        self.start_location = start_location
        self.end_location = end_location
        self.waypoints = waypoints
        self.distance = distance
        self.estimated_duration = estimated_duration
        self.created_at = created_at
        self.updated_at = updated_at
        
    @staticmethod
    def create_new_route(route_id, name, description, start_location, end_location, waypoints, distance, estimated_duration, created_at, updated_at):
        return Route (route_id=route_id,
                      route_uuid=None,
                      name=name,
                      description=description,
                      start_location=start_location,
                      end_location=end_location,
                      waypoints=waypoints,
                      distance=distance,
                      estimated_duration=estimated_duration,
                      created_at=created_at,
                      updated_at=updated_at)
    
    def update_route(self, start_location, end_location, waypoints, distance, estimated_duartion, update_at):
        if start_location:
            self.start_location = start_location
        if end_location:
            self.end_location = end_location
        if waypoints:
            self.waypoints = waypoints
        if distance:
            self.distance = distance
        if estimated_duartion:
            self.estimated_duration = estimated_duartion
        if update_at:
            self.updated_at = update_at