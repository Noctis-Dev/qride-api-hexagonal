# interface/controllers.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.infrastructure.user_repository import SQLAlchemyUserRepository
from app.users.application.services import UserService
from app.users.infrastructure.schemas import UserCreate, UserUpdate, User
from app.db import get_db

router = APIRouter()

# Ruta para actualizar un usuario
@router.patch("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user_repository = SQLAlchemyUserRepository(db)
    user_service = UserService(user_repository)

    try:
        user_service.update_user(user_id, full_name=user_update.full_name, phone_number=user_update.phone_number)
        updated_user = user_repository.get(user_id)
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/users", response_model=User)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user_repository = SQLAlchemyUserRepository(db)
    user_service = UserService(user_repository)

    try:
        new_user = user_service.create_user(
            email=user_create.email,
            password=user_create.password,
            full_name=user_create.full_name,
            phone_number=user_create.phone_number,
            user_rol=user_create.user_rol,
            profile_picture=user_create.profile_picture,
            current_points=user_create.current_points,
            balance=user_create.balance
        )
        return new_user
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invalid user role or other integrity constraint violation")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
