from fastapi import FastAPI
from app.db import engine, Base, SessionLocal
from app.roles.infrastructure.sql_repository import SQLAlchemyRoleRepository
from app.roles.application.services import RoleService
from app.users.infrastructure.controllers import router as user_router


# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

# Inicializar los roles
def initialize_roles():
    db = SessionLocal()
    role_repo = SQLAlchemyRoleRepository(db)
    role_service = RoleService(role_repo)
    role_service.initialize_roles()
    db.close()

initialize_roles()

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}