from pyrogram import filters
from HackSessionBot import app , START_PIC
from HackSessionBot.Helpers.data import PM_TEXT,PM_BUTTON,HACK_MODS,HACK_TEXT
from pyrogram.types import CallbackQuery


@app.on_message(filters.command("start") & filters.private)
async def _start(_, message):
    user = message.from_user.mention
    bot = (await _.get_me()).mention 
    await message.reply_photo(
       photo = START_PIC,
       caption = PM_TEXT.format(user, bot),
       reply_markup = PM_BUTTON) 


@app.on_message(filters.command("hack") & filters.private)
async def _hack(_, message):
    await message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


@app.on_callback_query(filters.regex("hack_btn"))
async def heck_callback(bot : app, query : CallbackQuery):
    await query.message.delete()
    await query.message.reply_text(HACK_TEXT,
              reply_markup = HACK_MODS) 


