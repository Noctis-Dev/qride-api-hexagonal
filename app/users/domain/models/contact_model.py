from datetime import datetime
from app.users.domain.models.user_model import User

class Contact: 
    def __init__(self, id: int, uuid: str, user: User, email: str, phone_number: str, name: str, created_at: datetime):
        self.id = id
        self.uuid = uuid
        self.user = user
        self.email = email
        self.phone_number = phone_number
        self.name = name
        self.created_at = created_at
        
