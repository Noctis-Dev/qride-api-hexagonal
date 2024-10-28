from app.users.domain.repositories.contact_repository import ContactRepository
from app.users.domain.models.contact_model import Contact

class CreateContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def execute(self, contact: Contact):
        return self.contact_repository.save(contact)