from sqlalchemy import Column, Integer, String, Boolean
from .config import Base


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
