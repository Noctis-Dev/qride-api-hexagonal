from app.users.domain.repositories.contact_repository import ContactRepository
from app.users.domain.models.contact_model import Contact
from app.users.application.schemas.requests.contact_request import ContactRequest
from app.users.application.mappers.contact_mapper import ContactMapper

class CreateContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, request: ContactRequest) -> Contact:
        contact = ContactMapper.to_domain(request)
        return self.contact_repository.save(contact)