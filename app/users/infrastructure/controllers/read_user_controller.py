from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.read_user_use_case import ReadUserUseCase
from app.users.infrastructure.schemas import UserUpdate, User
from app.db import get_db

class ReadUserController:
    def __init__(self) -> None:
        self.use_case = ReadUserUseCase()
        pass

    router = APIRouter()

    @router.get('/users/{user_uuid}', response_model=User)
    def read_user(self, user_uuid: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        try:
            user = self.use_case.execute(user_uuid)
            return user
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))