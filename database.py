from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_link = "postgresql://user_name:password_value@db_service:5432/sample_db"

engine_object = create_engine(database_link)
session_factory = sessionmaker(bind=engine_object, autoflush=False, autocommit=False)
base_class = declarative_base()