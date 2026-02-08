# creating the base class for SQLAlchemy models. This is used to define the structure of the database tables and to create the database schema.

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.db.models.user import User