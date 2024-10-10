from app.roles.domain.repository import RoleRepository
from app.roles.domain.models import Role

class RoleService:

    def __init__(self, role_repo: RoleRepository):
        self.role_repo = role_repo

    def initialize_roles(self):
        roles = ["passenger", "passenger_plus", "driver", "driver_admin", "checker"]
        for role_name in roles:
            role = self.role_repo.get_role_by_name(role_name)
            if not role:
                new_role = Role.create_new_role(role_name=role_name)  # Crear una instancia de Role
                self.role_repo.save(new_role) 