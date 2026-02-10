from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.user import get_user_by_email
from app.core.security import verify_password
from app.schemas.token import Token
from app.core.jwt import create_access_token

router = APIRouter()

@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return Token(access_token=access_token, token_type="bearer")