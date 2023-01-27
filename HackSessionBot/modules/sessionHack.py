from HackSessionBot import app
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall )
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 

@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ")
    if session:
        pass
    else:
        await query.message.reply_text("terminated")
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        system("rm -rf session.txt")
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


