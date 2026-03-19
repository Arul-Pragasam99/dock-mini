from fastapi import FastAPI
from database import engine_object
from models import base_class, UserEntity
from database import session_factory

app_instance = FastAPI()

base_class.metadata.create_all(bind=engine_object)

@app_instance.get("/")
def root_endpoint():
    return {"status": "db connected"}

@app_instance.post("/add/{name_input}")
def add_user(name_input: str):
    db_session = session_factory()
    user_object = UserEntity(name_value=name_input)
    db_session.add(user_object)
    db_session.commit()
    db_session.close()
    return {"added": name_input}