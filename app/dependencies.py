from fastapi import Depends
from .db.adapters.users import UserDatabase, TokenAdapter
from sqlalchemy.ext.asyncio import AsyncSession
from .db.models.users import User, Token, get_async_session
from fastapi_users.authentication.strategy import DatabaseStrategy


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield UserDatabase(session, User)


async def get_token_db(session: AsyncSession = Depends(get_async_session)):
    yield TokenAdapter(session, Token)


async def get_strategy(token=Depends(get_token_db)):
    return DatabaseStrategy(token, lifetime_seconds=3600)
