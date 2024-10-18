from fastapi_sqlalchemy_toolkit import make_partial_model
from pydantic import BaseModel


class BaseChild(BaseModel):
    pass


class ChildRead(BaseChild):
    id: int


class ChildCreate(BaseChild):
    pass


ChildUpdate = make_partial_model(ChildCreate)
