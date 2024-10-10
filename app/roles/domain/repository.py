from abc import ABC, abstractmethod
from typing import Optional
from app.roles.domain.models import Role

class RoleRepository(ABC):
    @abstractmethod
    def get(self, role_id: int) -> Optional[Role]:
        pass

    def get_role_by_name(self, role_name: str) -> Optional[Role]:
        pass

    @abstractmethod
    def save(self, role: Role) -> Role:
        pass