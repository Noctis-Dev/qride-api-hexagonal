from app.users.domain.repositories.contact_repository import ContactRepository

class ReadContactUseCase:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository
    
    def execute(self, contact_uuid: str):
        return self.contact_repository.get(contact_uuid)