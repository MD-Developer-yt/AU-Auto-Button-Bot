# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import time
import os

from pyrogram import (
    Client,
    filters
)

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from config import OWNER_ID
from database import count_users
from plugins.filters import admin_filter


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

START_TIME = time.time()

TOTAL_POSTS = 0


def owner(_, __, msg):

    return (
        msg.from_user
        and msg.from_user.id == OWNER_ID
    )


owner_filter = filters.create(owner)



def uptime():

    sec = int(time.time() - START_TIME)

    days, sec = divmod(sec, 86400)
    hours, sec = divmod(sec, 3600)
    minutes, sec = divmod(sec, 60)

    return (
        f"{days}d {hours}h {minutes}m {sec}s"
    )



async def stats_text():

    users = await count_users()

    return f"""
📊 <b>Bᴏᴛ Sᴛᴀᴛɪsᴛɪᴄs</b>

👤 Usᴇʀs : <code>{users}</code>

📤 Tᴏᴛᴀʟ Pᴏsᴛs : <code>{TOTAL_POSTS}</code>

🏓 Pɪɴɢ : <code>Online</code>

⚙️ Vᴇʀsɪᴏɴ : <code>v3 Stable</code>

⏳ Uᴘᴛɪᴍᴇ :
<code>{uptime()}</code>
"""


# ------------------------- #
# STATS COMMAND
# ------------------------- #

@Client.on_message(
    filters.command("stats") & admin_filter
)
async def stats(
    client,
    message
):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔄 Refresh Stats",
                    callback_data="refresh_stats"
                )
            ]
        ]
    )


    await message.reply_text(
        await stats_text(),
        reply_markup=buttons
    )



# ------------------------- #
# REFRESH BUTTON
# ------------------------- #

@Client.on_callback_query(
    filters.regex("refresh_stats")
)
async def refresh_stats(
    client,
    query
):

    if query.from_user.id != OWNER_ID:
        return


    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🔄 Refresh Stats",
                    callback_data="refresh_stats"
                )
            ]
        ]
    )


    await query.message.edit_text(
        await stats_text(),
        reply_markup=buttons
    )


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
