import motor.motor_asyncio
# from models import User

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.dev_test
user_collection = database.user