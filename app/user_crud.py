import time
from .config import settings
from . import models, schemas, utils
from .database import user_collection
from .models import UserIn, UserOut

async def fetch_one_user(user_id: str) -> UserOut:
    document = await user_collection.find_one({"_id": user_id})
    return document

async def fetch_all_users() -> list[UserOut]:
    users = []
    cursor = user_collection.find({})
    async for document in cursor:
        users.append(UserOut(**document))
    return users

async def create_user(user: UserIn) -> UserOut:
    document = user
    result = await user_collection.insert_one(document)
    return document

async def update_user(user_id: str, email: str) -> UserOut:
    await user_collection.update_one({"_id": user_id}, {"$set": {"email": email}})
    document = await user_collection.find_one({"_id": user_id})
    return document

async def remove_user(user_id: str)-> bool:
    await user_collection.delete_one({"_id": user_id})
    return True
