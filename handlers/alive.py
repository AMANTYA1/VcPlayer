import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME

# Awww
from modules.helper.filters import command
from modules.helper.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e5f8072af8b13ccb1628a.jpg",
        caption=f"""**
 ,      
    ...

  : [  ](https://t.me/ALONExSAD_BiO)
  : [  ](https://t.me/ALONExSAD_BiO)
    : [ ](https://t.me/ALONExBOY)

**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "       ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Alone"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e5f8072af8b13ccb1628a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f" ")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["ALONExMUSIC","ALONE", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e5f8072af8b13ccb1628a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f" ")
                ]
            ]
        ),
    )
