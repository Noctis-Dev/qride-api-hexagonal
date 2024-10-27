from app.users.domain.repositories.user_repository import UserRepository

class ReadUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_uuid: str):
        return self.user_repository.get(user_uuid)