from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
import schemas
from db import crud_user
from db.config import get_db

router = APIRouter(
    tags=['Users'],
    prefix="/user"
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.UserSchema, db: Session = Depends(get_db)):
    user = crud_user.create_user(request, db)
    return user


@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(user_id, db)
    return user
