from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Use this as a function patch when runnning Unit tests so it doesn't actually write to the
# production database
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()