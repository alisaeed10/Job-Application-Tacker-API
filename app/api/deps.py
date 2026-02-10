from app.db.session import SessionLocal
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from app.core.jwt import SECRET_KEY, ALGORITHM


#ensures that a new database session is created for each request and that it is properly closed after the request is completed. This is important for managing database connections and ensuring that resources are released appropriately.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(...)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    