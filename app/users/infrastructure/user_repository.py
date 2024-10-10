from typing import Optional
import uuid
from sqlalchemy.orm import Session
from app.users.domain.models import User
from app.users.domain.repositories import UserRepository
from app.users.infrastructure.user_model import User as UserModel

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, user_id: int) -> Optional[User]:
        user_model = self.db.query(UserModel).filter_by(user_id=user_id).first()
        if user_model:
            return User(
                user_id=user_model.user_id,
                email=user_model.email,
                full_name=user_model.full_name,
                phone_number=user_model.phone_number,
                password=user_model.password,
                user_rol=user_model.user_rol,
            )
        return None

    def save(self, user: User) -> User:
        user_model = UserModel(
            user_uuid=uuid.uuid4(),
            email=user.email,
            password=user.password,
            full_name=user.full_name,
            phone_number=user.phone_number,
            user_rol=user.user_rol,
            profile_picture=user.profile_picture,
            current_points=user.current_points,
            balance=user.balance,
        )
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model

    def update(self, user: User) -> None:
        user_model = self.db.query(UserModel).filter_by(user_id=user.user_id).first()
        if user_model:
            user_model.full_name = user.full_name
            user_model.phone_number = user.phone_number
            self.db.commit()
            self.db.refresh(user_model)
        else:
            raise ValueError(f"User with id {user.user_id} not found")
