from app.users.domain.repositories.role_repository import RoleRepository
from app.users.domain.models.role_model import Role

class InitializeUserRolesUseCase:
    def __init__(self, role_repository: RoleRepository):
        self.role_repository= role_repository

    def execute(self):
        roles = ["passenger", "passenger_plus", "driver", "driver_admin", "checker"]
        for role_name in roles:
            role = self.role_repository.get_role_by_name(role_name)
            if not role:
                new_role = Role.create_new_role(role_name=role_name)  # Crear una instancia de Role
                self.role_repository.save(new_role) 