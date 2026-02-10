from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash


# this creates a new user in the database. It takes a SQLAlchemy session and a UserCreate schema as input, hashes the password, and saves the user to the database.
def create_user(db: Session, user_in: UserCreate):
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()