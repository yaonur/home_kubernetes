from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .config import Base
from schemas import UserSchema,BlogSchema


class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    owner_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

    def __init__(self, blog: BlogSchema):
        self.title = blog.title
        self.body = blog.body
        self.published = blog.published
        self.owner_id = blog.owner_id
        super(Blog, self).__init__()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")

    def __init__(self, user: UserSchema):
        self.name = user.name
        self.email = user.email
        self.password = user.password
        super(User, self).__init__()
