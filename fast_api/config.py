import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL_POSTGRE = os.getenv("DB_URL_POSTGRE")

engine = create_engine(DB_URL_POSTGRE)
SessionLocal = sessionmaker(autocommit=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
