from app.db.session import SessionLocal


#ensures that a new database session is created for each request and that it is properly closed after the request is completed. This is important for managing database connections and ensuring that resources are released appropriately.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()