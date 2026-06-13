# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import (
    Client,
    filters
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from config import (
    CHANNEL_ID,
    BUTTONS,
    OWNER_ID
)

from database import is_admin

from plugins.logs import send_log

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def allowed(uid):

    if uid == OWNER_ID:

        return True

    return await is_admin(uid)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                name,
                url=link
            )
            for name, link in row
        ]
        for row in BUTTONS
    ]
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
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
            "admins"
        ]
    )
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def post(_, message):


    if not await allowed(
        message.from_user.id
    ):

        return await message.reply_text(
            "❌ Not allowed"
        )


    try:

        if message.text:

            await _.send_message(
                CHANNEL_ID,
                message.text,
                reply_markup=keyboard
            )


        elif message.photo:

            await _.send_photo(
                CHANNEL_ID,
                message.photo.file_id,
                caption=message.caption or "",
                reply_markup=keyboard
            )


        elif message.video:

            await _.send_video(
                CHANNEL_ID,
                message.video.file_id,
                caption=message.caption or "",
                reply_markup=keyboard
            )


        elif message.document:

            await _.send_document(
                CHANNEL_ID,
                message.document.file_id,
                caption=message.caption or "",
                reply_markup=keyboard
            )


        await message.reply_text(
            "✅ Posted"
        )


        await send_log(
            _,
            f"📌 New Post\nUser: {message.from_user.id}"
        )


    except Exception as e:

        await message.reply_text(
            str(e)
        )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
