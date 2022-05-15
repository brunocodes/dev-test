import time
from .config import settings
from . import models, schemas, utils
from .database import user_collection
from .models import User

async def fetch_one_user(user_id: str) -> User:
    document = await user_collection.find_one({"_id": user_id})
    return document

async def fetch_all_users() -> list[User]:
    users = []
    cursor = user_collection.find({})
    async for document in cursor:
        users.append(User(**document))
    return users

async def create_user(user: User) -> User:
    document = user
    result = await user_collection.insert_one(document)
    return document

async def update_user(user_id: str, email: str) -> User:
    await user_collection.update_one({"_id": user_id}, {"$set": {"email": email}})
    document = await user_collection.find_one({"_id": user_id})
    return document

async def remove_user(user_id: str)-> bool:
    await user_collection.delete_one({"_id": user_id})
    return True
