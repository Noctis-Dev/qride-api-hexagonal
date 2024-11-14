from app.users.domain.models.contact_model import Contact
from app.users.application.schemas.requests.contact_request import ContactRequest
from app.users.application.schemas.responses.contact_response import ContactResponse

class ContactMapper:
    @staticmethod
    def to_domain(contact: ContactRequest) -> Contact:
        return Contact(
            id=None,
            uuid=None,
            user=None,
            email=getattr(contact, 'email', None),
            phone_number=getattr(contact, 'phone', None),
            name=contact.name,
            created_at=None
        )

    @staticmethod
    def to_dict(contact: Contact) -> dict:
        return {
            'id': contact.id,
            'uuid': contact.uuid,
            'user': contact.user,
            'email': contact.email,
            'phone_number': contact.phone_number,
            'name': contact.name,
            'created_at': contact.created_at
        }
    
    @staticmethod
    def to_response(contact: Contact) -> ContactResponse:
        return ContactResponse(
            name=contact.name,
        )