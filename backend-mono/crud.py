from sqlalchemy.orm import Session
from . import models, schemas
from .core.security import get_password_hash, verify_password

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password, is_admin=user.is_admin)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user
