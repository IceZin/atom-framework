from sqlalchemy import create_engine

from ..env import DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE

engine = create_engine(
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE}",
    echo=False
)

from .sessions import Session, SessionQueries
from .users import User, UserQueries