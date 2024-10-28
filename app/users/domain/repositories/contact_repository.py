from abc import ABC, abstractmethod
from typing import Optional
from app.users.domain.models.contact_model import Contact

class ContactRepository(ABC):
    @abstractmethod
    def get(self, contact_uuid: str) -> Optional[Contact]:
        pass

    @abstractmethod
    def save(self, contact: Contact) -> None:
        pass