from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, Unique=True, index=True)
    hash_password = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    items = relationship("Item", back_populates="owner")