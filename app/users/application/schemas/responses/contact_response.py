from pydantic import BaseModel

class ContactResponse(BaseModel):
    name: str