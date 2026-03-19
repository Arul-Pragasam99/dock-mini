from sqlalchemy import Column, Integer, String
from database import base_class

class UserEntity(base_class):
    __tablename__ = "user_table"

    id_value = Column(Integer, primary_key=True, index=True)
    name_value = Column(String, index=True)