from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.delete_user_use_case import DeleteUserUseCase
from app.users.infrastructure.schemas import User
from app.db import get_db

class DeleteUserController:
    def __init__(self) -> None:
        self.use_case = DeleteUserUseCase()
        pass

    router = APIRouter()

    @router.delete('/users/{user_uuid}', response_model=User)
    def delete_user(self, user_uuid: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        try:
            self.use_case.execute(user_uuid)
            deleted_user = user_repository.get(user_uuid)
            return deleted_user
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))