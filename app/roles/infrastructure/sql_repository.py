from sqlalchemy.orm import Session
from typing import Optional
from app.roles.domain.models import Role
from app.roles.infrastructure.sql_model import Role as RoleModel
from app.roles.domain.repository import RoleRepository
import uuid

class SQLAlchemyRoleRepository(RoleRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_role_by_name(self, role_name: str):
        return self.db.query(RoleModel).filter(RoleModel.role_name == role_name).first()
    
    def get(self, role_id: int) -> Optional[Role]:
        role_model = self.db.query(RoleModel).filter_by(role_id=role_id).first()
        if role_model:
            return Role(
                role_id=role_model.rol_id,
                role_name=role_model.role_name,
                role_uuid=role_model.role_uuid
            )
        return None

    def save(self, role: Role):
        role_uuid = str(uuid.uuid4()) 
        role = RoleModel(role_name=role.role_name, role_uuid=role_uuid)
        self.db.add(role)
        self.db.commit()
        self.db.refresh(role)
        return role