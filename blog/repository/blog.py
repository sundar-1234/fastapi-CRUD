from .. import models,database
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status,Response

get_db = database.get_db

def create_blog(db:Session,request):
    new_blog = models.Blog(title=request.title, body = request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_blog(id,response,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
          raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    return blog

def delete(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updateBlog(id,request,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'updated'