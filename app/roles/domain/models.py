class Role:
    def __init__(self, role_id: int, role_name: str, role_uuid: str):
        self.role_id = role_id
        self.role_name = role_name
        self.role_uuid = role_uuid

    @staticmethod
    def create_new_role(role_name: str):
        return Role(role_id=None, role_name=role_name, role_uuid=None)