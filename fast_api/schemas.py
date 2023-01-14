from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class BlogSchema(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    owner_id: int

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[BlogSchema]

    class Config:
        orm_mode = True


class ShowBlog(BlogSchema):
    creator: ShowUser
    # pass


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

# class RequestBlog(BaseModel):
#     parameter: BlogSchema = Field(...)
#
#
# class Response(GenericModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]
