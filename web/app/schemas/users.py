from typing import Optional, TypeVar
from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    email: Optional[EmailStr] = None


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: Optional[EmailStr] = None


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


UC = TypeVar('UC', bound=UserCreate)
