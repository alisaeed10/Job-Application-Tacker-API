from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user

router = APIRouter()

@router.post("/", response_model=UserOut)
def create_user_endpoint(
    user_in: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user_in)

@router.post("/login")
def login_user():
    return {"message": "Login endpoint"}