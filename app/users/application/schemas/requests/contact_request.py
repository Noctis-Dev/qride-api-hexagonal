from pydantic import BaseModel
from typing import Optional

class ContactRequest(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
