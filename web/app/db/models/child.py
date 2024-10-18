from .base import Base, IDMixin
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

class Child(IDMixin, Base):
    __tablename__ = 'child'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(256), unique=True, nullable=False, index=True)