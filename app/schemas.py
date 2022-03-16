from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(Post):
    pass


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class PostResponse(Post):
    id: int
    created_at: datetime
    user_id: int
    owner: UserResponse

    class Config:
        orm_mode = True


class User(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
