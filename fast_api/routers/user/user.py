from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
import schemas
from db import crud_user
from db.config import get_db

router = APIRouter()


@router.post('/user', response_model=schemas.ShowUser, tags=['users'])
def create_user(request: schemas.UserSchema, db: Session = Depends(get_db)):
    user = crud_user.create_user(request, db)
    return user


@router.get('/user/{user_id}', response_model=schemas.ShowUser, tags=['users'])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user(user_id, db)
    return user
