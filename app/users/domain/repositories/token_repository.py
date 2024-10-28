from abc import ABC, abstractmethod
from typing import Optional
from app.users.domain.models.token_model import Token

class TokenRepository(ABC):
    @abstractmethod
    def get(self, token_uuid: str) -> Optional[Token]:
        pass

    @abstractmethod
    def save(self, token: Token) -> None:
        pass