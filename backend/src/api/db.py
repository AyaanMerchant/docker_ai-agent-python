import os
import sqlmodel
from sqlmodel import create_engine, Session

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise NotImplementedError("DATABASE_URL is not set")

engine = sqlmodel.create_engine(DATABASE_URL)

def init_db():
    print("Initializing database")
    sqlmodel.SQLModel.metadata.create_all(engine)

def get_session():
    with sqlmodel.Session(engine) as session:
        yield session