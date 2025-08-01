from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'sundar'}}

# @app.get('/about')
# def about():
#     return {'data':'about page'}

@app.get('/blog') 
def blog(limit,published:bool):
    if published:
        return {'data':f'{limit} published from list'}
    else:
        return {'data':f'{limit} unpublished from list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'unpublished'} 

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}

class Blog(BaseModel):
    title:str
    body:str
    published: Optional[bool] = None

@app.post('/blog')
def createblog(request:Blog):
    return request
    return {'data':'blog created'}



