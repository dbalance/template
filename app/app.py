from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from .settings import BASE_DIR
from .db.models.users import User, create_db_and_tables
from .schemas.users import UserCreate, UserRead, UserUpdate
from .authentificate.users import auth_backend, current_active_user, fastapi_users

templates = Jinja2Templates(directory= BASE_DIR / 'templates')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request=request, name='home.html')
