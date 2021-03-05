from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.START_TEXT.format(message.from_user.mention),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔰 HELP 🔰", callback_data="help"), InlineKeyboardButton("🔰 ABOUT 🔰", callback_data="about")]]),
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(    
        chat_id=message.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔰 ABOUT 🔰", callback_data="about"), InlineKeyboardButton("🔰 HOME 🔰", callback_data="home")]]),
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["about"]))
async def about(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔰 HELP 🔰", callback_data="help"), InlineKeyboardButton("🔰 HOME 🔰", callback_data="home")]]),
        reply_to_message_id=message.message_id
    )
