from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext


# REGISTRATION
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# LOGIN
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username_or_email: str, password: str):
    user = db.query(models.User).filter(
        (models.User.username == username_or_email) |
        (models.User.email == username_or_email)
    ).first()
    
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user