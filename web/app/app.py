from fastapi import Depends, FastAPI, Request

from .api.api import api

from .db.setup import create_db_and_tables
from .conf import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    await create_db_and_tables(engine)
    yield



app = FastAPI(lifespan=lifespan)


app.include_router(api, prefix='/api')

