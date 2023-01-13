from typing import Callable, List, Any
from sqlalchemy.orm import Session
from .model import Blog
from schemas import BlogSchema


def get_blog(db: Session, skip: int = 0, limit: int = 100) -> Callable[[], list[Blog]]:
    return db.query(Blog).offset(skip).limit(limit).all


def get_blog_by_id(db: Session, blog_id: int) -> Blog:
    return db.query(Blog).filter(Blog.id == blog_id).first()


def create_blog(db: Session, blog: BlogSchema) -> Blog:
    _blog = Blog(title=blog.title,body=blog.body,published=blog.published)
    db.add(_blog)
    db.commit()
    db.refresh(_blog)
    return _blog


def remove_blog(db: Session, blog_id: int):
    _blog = get_blog_by_id(db=db, blog_id=blog_id)
    db.delete(_blog)
    db.commit()


def update_blog(db: Session, blog_id: int, title: str, body: str, published: bool) -> Blog:
    _blog = get_blog_by_id(db=db, blog_id=blog_id)
    _blog.title = title
    _blog.body = body
    _blog.published = published
    db.commit()
    db.refresh(_blog)
    return _blog
