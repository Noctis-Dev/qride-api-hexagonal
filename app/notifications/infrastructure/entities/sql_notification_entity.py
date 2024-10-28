from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.notifications.domain.enums.notification_type import NotificationType
from app.db import Base  

class SQLNotification(Base):
    __tablename__ = 'notifications'

    notification_id = Column(BigInteger, primary_key=True)
    notification_uuid = Column(String(36), nullable=False)
    user_id = Column(ForeignKey('users.user_id'), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    message = Column(String(255), nullable=False)
    created_at = Column(Integer, nullable=False)
    notification_type = Column(Enum(NotificationType), nullable=False)    
    
    relationship('User')