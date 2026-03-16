import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
session = sessionmaker(bind=engine, autoflush=False, autocommit=False)