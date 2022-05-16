import motor.motor_asyncio
from . import models, schemas
from .database import user_collection


async def fetch_one_user(user_id: int) -> schemas.UserOut:
    document = await user_collection.find_one({"user_id": user_id},{"_id": 0})
    return document

async def create_user(user: models.UserIn) -> schemas.UserOut:
    result = await user_collection.insert_one({**user.dict()})
    return user

async def update_user(user: models.UserUpdate) -> schemas.UserOut:
    print("User: ", user)
    await user_collection.update_one({"user_id": user.user_id}, {"$set": {**user.dict()}})
    document = await user_collection.find_one({"user_id": user.user_id},{"_id": 0})
    print("Doc: ", document)
    return document

async def remove_user(user_id: int) -> int:
    del_res = await user_collection.delete_one({"user_id": user_id})
    return del_res.deleted_count
