from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from schemas import BlogSchema, ShowBlog
from db import crud_blog
from db.config import get_db

router = APIRouter(tags=["blogs"], prefix="/blog")


@router.get('/', response_model=list[ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = crud_blog.get_blogs(db)
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog_req: BlogSchema, db: Session = Depends(get_db)):
    blog = crud_blog.create_blog(db, blog_req)
    return blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud_blog.remove_blog(db, blog_id)
    return "done"


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(updated_blog: BlogSchema, blog_id: int, db: Session = Depends(get_db)):
    blog = crud_blog.update_blog(db, blog_id, updated_blog.title, updated_blog.body, updated_blog.published)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with {blog_id} not found")
    return 'updated'


@router.get('/{blog_id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_blog_by_id(response: Response, blog_id: int, db: Session = Depends(get_db)):
    blog = crud_blog.get_blog_by_id(db, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {blog_id} is not available ")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {blog_id} is not available'}
    return blog
