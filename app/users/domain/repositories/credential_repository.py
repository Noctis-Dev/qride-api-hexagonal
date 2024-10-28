from abc import ABC, abstractmethod
from typing import Optional
from app.users.domain.models.credential_model import Credential

class CredentialRepository(ABC):
    @abstractmethod
    def get(self, credential_uuid: str) -> Optional[Credential]:
        pass

    @abstractmethod
    def save(self, credential: Credential) -> None:
        pass