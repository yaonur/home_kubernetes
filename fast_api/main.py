from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import crud
from schemas import BlogSchema
from db import model
from db.config import engine, get_db

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def index():
    return {"hy": "ss"}


@app.get('/blog')
def index(published: bool, limit=10, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db '}
    return {'data': f'{limit} unpublished blogs from the db'}


@app.get('/blog/unbuplished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{blog_id}')
def blog(blog_id: int):
    return {"blog": {blog_id}}


@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments with id
    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog(blog_req: BlogSchema, db: Session = Depends(get_db)):
    crud.create_blog(db, blog_req)
    return {'title': blog_req.title, 'body': blog_req.body}
