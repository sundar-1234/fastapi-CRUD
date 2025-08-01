from passlib.context import CryptContext
from ..import models
from sqlalchemy.orm import Session
from fastapi import HTTPException,status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create(db:Session,request):
    hash_pass = pwd_context.hash(request.password)
    user = models.User(name = request.name,email = request.email,password = hash_pass)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def getall(db:Session):
    users = db.query(models.User).all()
    return users

def get(id,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found')
    return user
