import motor.motor_asyncio
# from models import User
from .config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(settings.database_link)
database = client.dev_test
user_collection = database.user