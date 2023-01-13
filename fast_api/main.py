from typing import Optional

import starlette.exceptions
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from schemas import BlogSchema
from db import models, crud
from db.config import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def index():
    return {"Blogger": "ss"}


@app.get('/blogs')
def get_blogs(db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db)
    return blogs


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog_req: BlogSchema, db: Session = Depends(get_db)):
    blog = crud.create_blog(db, blog_req)
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.remove_blog(db, blog_id)
    return 'done'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(updated_blog: BlogSchema, blog_id: int, db: Session = Depends(get_db)):
    blog = crud.update_blog(db, blog_id, updated_blog.title, updated_blog.body, updated_blog.published)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {blog_id} not found")
    return 'updated'


@app.get('/blog/unbuplished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{blog_id}', status_code=status.HTTP_200_OK)
def get_blog_by_id(response: Response, blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog_by_id(db, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {blog_id} is not available ")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {blog_id} is not available'}
    return {blog}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments with id
    return {'data': {'1', '2'}}
