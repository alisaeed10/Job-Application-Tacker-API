import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID # for uniqueness and indexing of the id field
from sqlalchemy.sql import func

from app.db.base import Base


# defining the User model, which represents the users table in the database. It includes fields for id, email, hashed_password, created_at, and updated_at. The id field is a UUID that is generated automatically when a new user is created. The email field is unique and indexed for efficient querying. The created_at and updated_at fields are automatically set to the current timestamp when a user is created or updated.
class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())     