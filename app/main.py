from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from contextlib import asynccontextmanager
from redis.asyncio import Redis
from dotenv import load_dotenv
from app.db import engine, Base, SessionLocal
from app.users.infrastructure.repositories.sql_role_repository import SQLAlchemyRoleRepository
from app.users.application.use_cases.Initialize_user_roles_use_case import InitializeUserRolesUseCase
from app.users.infrastructure.controllers.create_user_controller import CreateUserController
from app.users.infrastructure.controllers.list_users_controller import ListUsersController
from app.users.infrastructure.controllers.update_user_controller import UpdateUserController
from app.users.infrastructure.controllers.delete_user_controller import DeleteUserController
from app.users.infrastructure.controllers.read_user_by_email_controller import ReadUserByEmailController
from app.users.infrastructure.controllers.read_user_controller import ReadUserController
from app.vehicles.infrastructure.controllers.create_vehicle_controller import CreateVehicleController
from app.vehicles.infrastructure.controllers.list_vehicles_controller import ListVehiclesController
from app.vehicles.infrastructure.controllers.list_vehicles_by_route_controller import ListVehicleByRouteController
from app.vehicles.infrastructure.controllers.list_vehicle_users_by_user_controller import ListVehicleUsersByUserController
from app.vehicles.infrastructure.controllers.list_vehicle_users_by_vehicle_controller import ListVehicleUsersByVehicleController
from app.vehicles.infrastructure.controllers.update_vehicle_controller import UpdateVehicleController
from app.vehicles.infrastructure.controllers.delete_vehicle_controller import DeleteVehicleController
from app.users.infrastructure.controllers.create_contact_controller import CreateContactController

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# Crear la base de datos y las tablas
Base.metadata.create_all(bind=engine)

# Inicializar los roles
def initialize_roles():
    db = SessionLocal()
    role_repo = SQLAlchemyRoleRepository(db)
    role_service = InitializeUserRolesUseCase(role_repo)
    role_service.execute()
    db.close()
    
initialize_roles()

app = FastAPI()
    
# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(CreateUserController.router, prefix="/api/v1")
app.include_router(ListUsersController.router, prefix="/api/v1")
app.include_router(UpdateUserController.router, prefix="/api/v1")
app.include_router(DeleteUserController.router, prefix="/api/v1")
app.include_router(ReadUserByEmailController.router, prefix="/api/v1")
app.include_router(ReadUserController.router, prefix="/api/v1")
app.include_router(CreateVehicleController.router, prefix="/api/v1")
app.include_router(ListVehiclesController.router, prefix="/api/v1")
app.include_router(ListVehicleByRouteController.router, prefix="/api/v1")
app.include_router(ListVehicleUsersByUserController.router, prefix="/api/v1")
app.include_router(ListVehicleUsersByVehicleController.router, prefix="/api/v1")
app.include_router(UpdateVehicleController.router, prefix="/api/v1")
app.include_router(DeleteVehicleController.router, prefix="/api/v1")
app.include_router(CreateContactController.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}
