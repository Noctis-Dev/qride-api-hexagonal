from abc import ABC, abstractmethod
from typing import Optional
from app.users.domain.models import User

class UserRepository(ABC):
    @abstractmethod
    def get(self, user_uuid: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_users(self, skip: int= 0, limit: int =100):
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user: User) -> None:
        pass