from fastapi import FastAPI
from app.db import engine, Base, SessionLocal
from app.roles.infrastructure.sql_repository import SQLAlchemyRoleRepository
from app.roles.application.services import RoleService
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
app.include_router(
    ListVehicleUsersByVehicleController.router, prefix="/api/v1")
app.include_router(UpdateVehicleController.router, prefix="/api/v1")
app.include_router(DeleteVehicleController.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Welcome to Qride API"}
