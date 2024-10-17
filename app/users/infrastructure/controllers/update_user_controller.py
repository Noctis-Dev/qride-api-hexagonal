from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.update_user_use_case import UpdateUserUseCase
from app.users.infrastructure.schemas import UserUpdate, User
from app.db import get_db

class UpdateUserController:
    def __init__(self,) -> None:
        self.use_case = UpdateUserUseCase()
        pass

    router = APIRouter()

    @router.put('/users/{user_uuid}', response_model=User)
    def update_user(self, user_uuid: str, user_update: UserUpdate, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        try:
            self.use_case.execute(user_uuid, full_name=user_update.full_name, phone_number=user_update.phone_number)
            updated_user = user_repository.get(user_uuid)
            return updated_user
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))