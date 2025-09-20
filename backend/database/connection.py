# backend/database/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.base import Base 
DataBase_URL = "sqlite:///./backend/database/app.db"
engine = create_engine(DataBase_URL, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from backend.models import user
def init_db():
    Base.metadata.create_all(bind=engine)

init_db()
