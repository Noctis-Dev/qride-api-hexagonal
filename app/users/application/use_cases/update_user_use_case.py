from app.users.domain.repositories import UserRepository

class UpdateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_uuid: str, full_name: str = None, phone_number: str = None):
        user = self.user_repository.get(user_uuid)
        if not user:
            raise ValueError(f"User with id {user_uuid} not found")
        user.update_info(full_name, phone_number)
        self.user_repository.update(user)