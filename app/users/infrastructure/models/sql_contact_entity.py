from sqlalchemy import Column, BigInteger, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from app.db import Base  

class ContactEntity(Base):
    __tablename__ = 'contacts'

    contact_id = Column(BigInteger, primary_key=True)
    contact_uuid = Column(String(36), nullable=False)
    email = Column(String(50))
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(15))
    user_id = Column(ForeignKey('users.user_id'), index=True)

    user = relationship('User')