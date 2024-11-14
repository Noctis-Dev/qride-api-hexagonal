from typing import List, Optional
import uuid
from sqlalchemy.orm import Session
from app.users.domain.models.contact_model import Contact
from app.users.domain.repositories.contact_repository import ContactRepository
from app.users.infrastructure.models.sql_contact_entity import ContactEntity

class SQLContactRepository(ContactRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, contact_uuid: str) -> Optional[Contact]:
        contact_entity = self.db.query(ContactEntity).filter(
            ContactEntity.contact_uuid == contact_uuid).first()
        if contact_entity:
            return Contact(
                contact_id=contact_entity.contact_id,
                contact_uuid=contact_entity.contact_uuid,
                email=contact_entity.email,
                name=contact_entity.full_name,
                phone_number=contact_entity.phone_number,
                user_id=contact_entity.user_id
            )
        return None
    
    def save(self, contact: Contact) -> None:
        contact_entity = ContactEntity(
            contact_uuid=uuid.uuid4(),
            email=contact.email,
            full_name=contact.name,
            phone_number=contact.phone_number,
        )
        self.db.add(contact_entity)
        self.db.commit()
        self.db.refresh(contact_entity)
        return None