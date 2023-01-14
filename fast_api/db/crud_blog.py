from typing import Callable, List, Any
from sqlalchemy.orm import Session
from .models import Blog
from schemas import BlogSchema


def get_blogs(db: Session, skip: int = 0, limit: int = 100) -> List[Blog]:
    return db.query(Blog).offset(skip).limit(limit).all()


def get_blog_by_id(db: Session, blog_id: int) -> Blog:
    return db.query(Blog).filter(Blog.id == blog_id).first()


def create_blog(db: Session, blog: BlogSchema) -> Blog:
    _blog = Blog(blog)
    db.add(_blog)
    db.commit()
    db.refresh(_blog)
    return _blog


def remove_blog(db: Session, blog_id: int) -> Blog:
    _blog = get_blog_by_id(db=db, blog_id=blog_id)
    db.delete(_blog)
    db.commit()
    return _blog


def update_blog(db: Session, blog_id: int, title: str, body: str, published: bool) -> Blog:
    _blog = get_blog_by_id(db=db, blog_id=blog_id)
    if not _blog:
        return _blog

    _blog.title = title
    _blog.body = body
    _blog.published = published
    db.commit()
    db.refresh(_blog)
    return _blog
