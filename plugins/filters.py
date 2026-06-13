# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #


from pyrogram import filters
from config import OWNER_ID
from database import is_admin


async def admin_check(_, __, msg):

    if not msg.from_user:
        return False

    if msg.from_user.id == OWNER_ID:
        return True

    return await is_admin(msg.from_user.id)


admin_filter = filters.create(admin_check)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
