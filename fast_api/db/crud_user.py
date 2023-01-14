from sqlalchemy.orm import Session

import schemas
from .models import User
from schemas import UserSchema
from .hashing import get_password_hash, verify_password


def create_user(user: UserSchema, db: Session):
    hashed_pass = get_password_hash(user.password)
    user.password = hashed_pass
    new_user = User(user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    return user
