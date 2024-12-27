from fastapi import APIRouter

from ..schemas.users import UserCreate, UserRead, UserUpdate
from ..authentificate.users import auth_backend, fastapi_users
from .endpoints.child import child_router
from .endpoints import m2m


api = APIRouter()

api.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
api.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
api.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
api.include_router(
    child_router,
    prefix='/child',
    tags=['child']
)

api.include_router(
    m2m.r,
    prefix='/m2m',
    tags=['m2m']
)