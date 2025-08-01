from fastapi import APIRouter,Depends,status,Response
from .. import schemas,database,oAuth2
from ..repository import blog
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)
get_db = database.get_db

@router.post('',status_code=status.HTTP_201_CREATED)
def createblog(request:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return blog.create_blog(db,request)

@router.get('',response_model=List[schemas.showBlog])
def getblogs(db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return blog.get_all(db)

@router.get('/{id}',status_code=200,response_model=schemas.showBlog)
def getblog(id,response:Response,db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return blog.get_blog(id,response,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return blog.delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(get_db),current_user:schemas.user = Depends(oAuth2.get_current_user)):
    return blog.updateBlog(id,request,db)
