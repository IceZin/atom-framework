from sqlalchemy import ForeignKey, select
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


class Session(Base):
    __tablename__ = "sessions"
    id: Mapped[int]
    uuid: Mapped[UUID] = mapped_column(primary_key=True)
    user_uuid: Mapped[UUID] = mapped_column(ForeignKey("users.uuid"))
    active: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())
        

class SessionQueries:
    @staticmethod
    def get_by_uuid(uuid: str) -> Session:
        with PgSession(engine) as session:
            query = select(Session).where(Session.uuid == uuid)
            result = session.execute(query).first()

            if result:
                return result[0]
            else:
                return None
