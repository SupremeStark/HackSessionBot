from pyrogram import filters
from HackSessionBot import app , START_PIC
from HackSessionBot.Helpers.data import PM_TEXT,PM_BUTTON


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
    user = message.from_user.mention
    bot = (await _.get_me()).mention 
    await message.reply_photo(
       photo = START_PIC,
       caption = HACK_TEXT.format(user, bot),
       reply_markup = PM_BUTTON) 

