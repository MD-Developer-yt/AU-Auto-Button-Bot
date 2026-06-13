# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters

from config import OWNER_ID
from database import get_users
from plugins.filters import admin_filter

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def owner(_, __, msg):

    return (
        msg.from_user
        and msg.from_user.id == OWNER_ID
    )


owner_filter = filters.create(owner)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("broadcast") & admin_filter
)
async def broadcast(
    client,
    message
):

    if not message.reply_to_message:

        return await message.reply_text(
            "Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Sᴇɴᴅ Bʀᴏᴀᴅᴄᴀsᴛ"
        )


    sent = 0
    failed = 0


    async for user in await get_users():

        try:

            await message.reply_to_message.copy(
                user["_id"]
            )

            sent += 1


        except:

            failed += 1



    await message.reply_text(
        f"""
✅️ Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ

Sᴇɴᴛ : {sent}
Fᴀɪʟᴇᴅ : {failed}
"""
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
