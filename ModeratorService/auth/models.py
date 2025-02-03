from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, TIMESTAMP, ARRAY, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from fastApiProject.ModeratorService.auth.utils import hashing
from fastApiProject.ModeratorService.auth.config.database import Base

class RegisteredUser(Base):
    __tablename__ = 'registered_user'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    studies = relationship("Study", back_populates="owner")


    def __init__(self, user_name, email, password):
        self.user_name = user_name
        self.email = email
        self.hashed_password = hashing.hash_password(password)
        self.created_at = datetime.now()

    def check_password(self, password):
        return hashing.verify_password(self.hashed_password, password)

class Study(Base):
    __tablename__ = 'study'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    study_name = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    research_objectives = Column(String, nullable=False)
    moderation_instructions = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('registered_user.id'))

    owner = relationship("RegisteredUser", back_populates="studies")


