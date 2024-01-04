from sqlalchemy import select
from sqlalchemy.orm import (
    Mapped,
    DeclarativeBase,
    Session as PgSession,
    mapped_column
)

from uuid import UUID
from datetime import datetime

from . import engine

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int]
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    verified: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())


class UserQueries:
    @staticmethod
    def get_by_uuid(uuid: str) -> User:
        with PgSession(engine) as session:
            query = select(User).where(User.uuid == uuid)
            result = session.execute(query).first()
            return result[0]