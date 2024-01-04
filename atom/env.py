import os

DATABASE = os.getenv("DATABASE", "nucleon")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "123")
