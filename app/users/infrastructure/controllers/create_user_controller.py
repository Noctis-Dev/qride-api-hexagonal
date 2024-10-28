from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.create_user_use_case import CreateUserUseCase
from app.users.infrastructure.schemas import UserCreate, User
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

class CreateUserController:
    router = APIRouter()

    @router.post('/users', response_model=User)
    def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = CreateUserUseCase(user_repository)
        logging.info(f"Trying to create user with email: {user_create.email}")
        try:
            new_user = use_case.execute(
                email=user_create.email,
                password=user_create.password,
                full_name=user_create.full_name,
                phone_number=user_create.phone_number,
                user_rol=user_create.user_rol,
                profile_picture=user_create.profile_picture,
                current_points=user_create.current_points,
                balance=user_create.balance
            )
            logging.info(f"User with email {user_create.email} created successfully.")
            return new_user
        except IntegrityError as e:
            db.rollback()
            logging.error(f"Erorr creating user {user_create.email} due to integrity constraints: {str(e)}")
            raise HTTPException(status_code=400, detail="Invalid user role or other integrity constraint violation")
        except ValueError as e:
            logging.error(f"Error creating user {user_create.email}: {str(e)}") 
            raise HTTPException(status_code=400, detail=str(e))