from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.read_user_by_email_use_case import ReadUserByEmailUseCase
from app.users.infrastructure.schemas import User
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

class ReadUserByEmailController:
    router = APIRouter()

    @router.get('/users/{email}', response_model=User)
    def read_user_by_email(email: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = ReadUserByEmailUseCase(user_repository)  
        logging.info(f"Attempting to find user with email: {email}")
        try:
            user = use_case.execute(email)
            logging.info(f"User with email {email} found.")
            return user
        except ValueError as e:
            logging.error(f"Error while searching for user with email {email}: {str(e)}")
            raise HTTPException(status_code=404, detail=str(e))