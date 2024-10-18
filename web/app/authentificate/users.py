from typing import Type

from fastapi import APIRouter
from fastapi_users import FastAPIUsers as APIUsers, schemas
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
)
from ..db.models.users import User
from ..dependencies.auth import get_strategy, get_user_manager

bearer_transport = BearerTransport(tokenUrl="api/auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_strategy,
)


class FastAPIUsers(APIUsers[User, int]):
    pass

fastapi_users = FastAPIUsers(get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
