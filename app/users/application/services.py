from app.users.domain.repositories import UserRepository
from app.users.domain.models import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, email: str, password: str, full_name: str, phone_number: str, user_rol: int, profile_picture: str, current_points: int, balance: float):
        new_user = User.create_new_user(email=email, password=password, full_name=full_name, phone_number=phone_number, user_rol=user_rol, profile_picture=profile_picture, current_points=current_points, balance=balance)
        return self.user_repository.save(new_user)

    def update_user(self, user_id: int, full_name: str = None, phone_number: str = None):
        user = self.user_repository.get(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        user.update_info(full_name, phone_number)
        self.user_repository.update(user)
