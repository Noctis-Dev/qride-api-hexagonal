from app.users.domain.repositories import UserRepository

class ReadUserByEmailUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str):
        return self.user_repository.get_user_by_email(email)