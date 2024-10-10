from typing import Type

from fastapi import APIRouter
from fastapi_users import FastAPIUsers as APIUsers, schemas
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
)
from ..db.models.users import User
from .manager import get_user_manager
from .register import get_register_router
from app.dependencies import get_strategy

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_strategy,
)


class FastAPIUsers(APIUsers[User, int]):

    def get_register_router(
            self, user_schema: Type[schemas.U], user_create_schema: Type[schemas.UC]
    ) -> APIRouter:
        return get_register_router(self.get_user_manager, user_schema, user_create_schema)


fastapi_users = FastAPIUsers(get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
