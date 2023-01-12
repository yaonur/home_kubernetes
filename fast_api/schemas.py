from typing import Optional, TypeVar, Generic
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class BlogSchema(BaseModel):
    title: str
    body: str
    published: Optional[bool]

    class Config:
        orm_mode = True


class RequestBlog(BaseModel):
    parameter: BlogSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
