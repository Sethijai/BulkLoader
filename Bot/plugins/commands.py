from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ..functions.filters import OWNER_FILTER


reply_markup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            text="DEVELOPER", url="https://t.me/REAL_HACKHEIST"),
        InlineKeyboardButton(text="HELP", url="https://t.me/onlymessages_bot"),
    ],
    [InlineKeyboardButton(text="🤩𝗝𝗢𝗜𝗡 𝗔𝗗𝗗𝗟𝗜𝗦𝗧", url="https://t.me/addlist/rMLA4niKz9xjYjg1")],
])


@Client.on_message(filters.command('start') & OWNER_FILTER & filters.private)
async def start(bot: Client, update: Message):
    await update.reply_text(text=f"I'm BulkLoader\nYou can upload list of links\n\n/help for more details!", quote=True, reply_markup=reply_markup)


@Client.on_message(filters.command('help') & OWNER_FILTER & filters.private)
async def help(bot: Client, update: Message):
    await update.reply_text(text=f"How to use BulkLoader?!\n\nMethods:\n- send a bunch of links.\n- send text file which contains links.\n\nNote: Make sure that each link is separated.\n\nSettings\n\n- `/thumbnail`: custom thumbnail. ex: reply to a photo or do `/thumbnail https...jpg`\n- `/caption`: custom thumbnail. ex: `/caption abc`\n\nNote: To clear thumbnail or the caption. do the command without args. ex: `/thumbnail` or `/caption`", quote=True, reply_markup=reply_markup)
