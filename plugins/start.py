
# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #

import asyncio

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from database import add_user
from config import (
    START_TEXT,
    ABOUT_TEXT
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

START_IMAGE = "https://graph.org/file/8cc7c4d5f0989b8efad96-f5d88bacd8e8049c9b.jpg"

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def buttons():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📢 Updates",
                    url="https://t.me/Anime_UpdatesAU"
                ),
                InlineKeyboardButton(
                    "👤 Owner",
                    url="https://t.me/Mr_Mohammed_29"
                )
            ],
            [
                InlineKeyboardButton(
                    "ℹ️ About",
                    callback_data="about"
                )
            ]
        ]
    )


# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("start")
    & filters.private
)

async def start(client, message):

    await add_user(
        message.from_user.id
    )


    m = await message.reply_text(
        "ᴍᴏɴᴋᴇʏ ᴅ ʟᴜғғʏ\nɢᴇᴀʀ 𝟻..."
    )


    for text in [
        "🎊",
        "🚀",
        "sᴜɴ ɢᴏᴅ ɴɪᴋᴀ!...",
        "✅ Started!"
    ]:
        await asyncio.sleep(0.5)
        await m.edit_text(text)


    await m.delete()


    await message.reply_sticker(
        "CAACAgQAAxkBAAPZafuA9gQjLstGU0j8kmlDj2-P2A0AAqoaAALVH9BRmAWPD58ZL6keBA"
    )


    await client.send_photo(
        message.chat.id,
        photo=START_IMAGE,
        caption=START_TEXT.format(
            mention=message.from_user.mention
        ),
        parse_mode="html",
        reply_markup=buttons()
    )


# ------------------------- #
# ABOUT
# ------------------------- #

@Client.on_callback_query(
    filters.regex("about")
)

async def about(client, query):

    about_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "🏠 Home",
                    callback_data="home"
                )
            ]
        ]
    )


    await query.message.delete()


    await client.send_photo(
        query.message.chat.id,
        photo=START_IMAGE,
        caption=ABOUT_TEXT,
        parse_mode="html",
        reply_markup=about_buttons
    )


# ------------------------- #
# HOME
# ------------------------- #

@Client.on_callback_query(
    filters.regex("home")
)

async def home(client, query):

    await query.message.delete()


    await client.send_photo(
        query.message.chat.id,
        photo=START_IMAGE,
        caption=START_TEXT.format(
            mention=query.from_user.mention
        ),
        parse_mode="html",
        reply_markup=buttons()
    )


# ------------------------- #
# Don't Remove Credit
# Owner @Mr_Mohammed_29
# ------------------------- #
