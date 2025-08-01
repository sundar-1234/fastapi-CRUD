from fastapi import APIRouter,Depends,status,HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..import schemas,database,models,oAuth2
from typing import List
from ..repository import user

router = APIRouter(
    prefix="/user", 
    tags=["users"]
)
get_db = database.get_db
    
@router.post('',response_model=schemas.showUser)
def create_user(request:schemas.user,db:Session = Depends(get_db)):
    return user.create(db,request)
    
@router.get('',response_model=List[schemas.showUser]  )
def getUser(db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return user.getall(db)

@router.get('/{id}',response_model=schemas.showUser,status_code=status.HTTP_200_OK)
def getUser(id,db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return user.get(id,db)