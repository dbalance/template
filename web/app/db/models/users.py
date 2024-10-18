from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from .base import Base, IDMixin


class User(IDMixin, SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'users'
    username: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)
    email: Mapped[str | None] = mapped_column(String(320), unique=True, nullable=True, index=True)


class Token(SQLAlchemyBaseAccessTokenTable[int], Base):
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='cascade'), nullable=False)
