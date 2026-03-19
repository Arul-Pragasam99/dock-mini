from fastapi import FastAPI
from database import engine_object, session_factory
from models import base_class, UserEntity
from cache_store import cache_client
import json

app_instance = FastAPI()

base_class.metadata.create_all(bind=engine_object)

@app_instance.get("/user/{user_id}")
def get_user(user_id: int):
    cache_key_value = f"user:{user_id}"

    cached_data = cache_client.get(cache_key_value)

    if cached_data:
        return {"source": "cache", "data": json.loads(cached_data)}

    db_session = session_factory()
    user_object = db_session.query(UserEntity).filter(UserEntity.id_value == user_id).first()
    db_session.close()

    if not user_object:
        return {"error": "not found"}

    response_payload = {
        "id": user_object.id_value,
        "name": user_object.name_value
    }

    cache_client.set(cache_key_value, json.dumps(response_payload), ex=60)

    return {"source": "db", "data": response_payload}