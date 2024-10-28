from datetime import datetime
from app.users.domain.enums.token_type import TokenType

class Token:
    def __init__(self, id: int, uuid: str, access_token: str, refresh_token: str, 
                 access_expires_at: datetime, refresh_expires_at: datetime, token_type: TokenType):
        self.id = id
        self.uuid = uuid
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.access_expires_at = access_expires_at
        self.refresh_expires_at = refresh_expires_at
        self.token_type = token_type

    def is_expired(self):
        return self.access_expires_at < datetime.now()

   