from sqlalchemy.orm import Session
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.conf import settings

engine = create_engine(settings.DB_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
