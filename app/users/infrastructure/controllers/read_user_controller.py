from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.read_user_use_case import ReadUserUseCase
from app.users.infrastructure.schemas import UserUpdate, User
from app.db import get_db
import logging
import os

log_dir = "var/log"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'myapp.log'), 
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class ReadUserController:
    router = APIRouter()

    @router.get('/users/{user_uuid}', response_model=User)
    def read_user(user_uuid: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = ReadUserUseCase(user_repository)
        logging.info(f"Attempting to find user with UUID: {user_uuid}")
        try:
            user = use_case.execute(user_uuid)
            logging.info(f"User with UUID {user_uuid} found.")
            return user
        except ValueError as e:
            logging.error(f"Error while searching for user with UUID {user_uuid}: {str(e)}")
            raise HTTPException(status_code=404, detail=str(e))