# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

client = AsyncIOMotorClient(
    MONGO_URI
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

db = client["AutoButtonBot"]


users = db.users
admins = db.admins

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def add_user(uid):

    if not await users.find_one(
        {"_id": uid}
    ):

        await users.insert_one(
            {
                "_id": uid
            }
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def count_users():

    return await users.count_documents({})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def add_admin(uid):

    if not await admins.find_one(
        {"_id": uid}
    ):

        await admins.insert_one(
            {
                "_id": uid
            }
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def remove_admin(uid):

    await admins.delete_one(
        {
            "_id": uid
        }
    )



async def is_admin(uid):

    return bool(
        await admins.find_one(
            {
                "_id": uid
            }
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_admins():

    data = []

    async for x in admins.find():

        data.append(
            x["_id"]
        )

    return data

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def get_users():

    return users.find({})

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
