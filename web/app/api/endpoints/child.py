from ...fastapi_crud_toolkit import FastAPICrudToolkit
from fastapi import APIRouter
from fastapi_sqlalchemy_toolkit import ModelManager
from ...dependencies.session import get_async_session
from ...db.models import Child
from ...schemas.child import ChildCreate, ChildUpdate, ChildRead
from ...authentificate.users import fastapi_users

manager = ModelManager(Child)

child_router = FastAPICrudToolkit(
    manager,
    get_async_session,
    ChildRead,
    ChildCreate,
    ChildUpdate,
    fastapi_users.authenticator
).get_crud_router()



@child_router.get('/like')
async def like():
    return {'hello': '2'}