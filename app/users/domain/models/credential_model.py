from datetime import datetime
from app.users.domain.models.contact_model import Contact
from app.users.domain.models.token_model import Token

class Credential:
    def __init__(self, id: int, uuid: str, password: str, created_at: datetime, verified_at: datetime, token: Token, contact: Contact):
        self.id = id
        self.uuid = uuid
        self.password = password
        self.created_at = created_at
        self.verified_at = verified_at
        self.token = token
        self.contact = contact