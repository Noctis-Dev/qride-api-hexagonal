from datetime import datetime, timedelta
import random
from app.users.domain.enums.token_type import TokenType

class Token:
    def __init__(self, id: int, uuid: str, access_token: str, access_expires_at: datetime, token_type: TokenType):
        self.id = id
        self.uuid = uuid
        self.access_token = access_token
        self.access_expires_at = access_expires_at
        self.token_type = token_type

    def is_expired(self):
        return self.access_expires_at < datetime.now()
    
    @staticmethod
    def create_verification_token():
        token = f"{random.randint(1000, 9999)}"  # Generar un token de 4 dígitos
        expires_at = datetime.now() + timedelta(minutes=20)
        return Token(id=None, uuid=None, token=token, expires_at=expires_at, token_type=TokenType.VERIFICATION)