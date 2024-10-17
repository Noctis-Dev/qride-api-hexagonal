from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db import Base
from app.vehicles.infrastructure.models.sql_route_model import Route

class SQLVehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_id = Column(BigInteger, primary_key=True)
    vehicle_uuid = Column(String(36), nullable=False)
    route_id = Column(ForeignKey('routes.route_id'), nullable=False, index=True)
    current_location = Column(String(255))
    status = Column(String(255))

    route = relationship('Route')