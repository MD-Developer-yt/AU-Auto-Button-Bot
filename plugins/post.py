# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import plugins.thumbnail as thumb
import plugins.stats as stats

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import CHANNEL_ID, BUTTONS, OWNER_ID
from database import is_admin
from plugins.logs import send_log


# ------------------------- #
# ADMIN CHECK
# ------------------------- #

async def allowed(uid):
    if uid == OWNER_ID:
        return True
    return await is_admin(uid)


keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(name, url=link)
            for name, link in row
        ]
        for row in BUTTONS
    ]
)


# ------------------------- #
# POST SYSTEM
# ------------------------- #

@Client.on_message(
    filters.private
    & ~filters.command(
        [
            "start",
            "stats",
            "broadcast",
            "addadmin",
            "removeadmin",
            "admins",
            "thumbnail"
        ]
    )
)
async def post(_, message):

    if not await allowed(message.from_user.id):
        return await message.reply_text("❌ Not allowed")

    try:

        # TEXT
        if message.text:

            await _.send_message(
                CHANNEL_ID,
                message.text,
                reply_markup=keyboard
            )

        # PHOTO
        elif message.photo:

            await _.send_photo(
                CHANNEL_ID,
                photo=message.photo.file_id,
                caption=message.caption or "",
                reply_markup=keyboard
            )

        # VIDEO (FIXED THUMBNAIL HANDLING)
        elif message.video:

            await _.send_video(
                CHANNEL_ID,
                video=message.video.file_id,
                caption=message.caption or "",
                thumb=thumb.THUMBNAIL if thumb.THUMBNAIL else None,
                reply_markup=keyboard
            )

        # DOCUMENT (FIXED THUMBNAIL HANDLING)
        elif message.document:

            await _.send_document(
                CHANNEL_ID,
                document=message.document.file_id,
                caption=message.caption or "",
                thumb=thumb.THUMBNAIL if thumb.THUMBNAIL else None,
                reply_markup=keyboard
            )

        # UPDATE STATS
        stats.TOTAL_POSTS += 1

        await message.reply_text("✅ Posted")

        # LOG FIX (important safe call)
        await send_log(_, f"📌 New Post\nUser: {message.from_user.id}")

    except Exception as e:
        await message.reply_text(str(e))


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
