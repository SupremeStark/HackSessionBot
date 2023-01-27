from HackSessionBot import app
from pyrogram import filters 
from HackSessionBot.Helpers.steve import users_gc
from HackSessionBot.Helpers.data 

@app.on_callback_query(filters.regex("A"))
async def a_callback(client , message):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"ɴᴏᴡ ɢɪᴠᴇ ᴍᴇ ᴛʜᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴏғ ᴛʜᴀᴛ ᴜsᴇʀ")
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        system("rm -rf session.txt")
    else:
        await query.message.reply_text(ch + "\n\nᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ᴍᴇ , ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴛᴏ ᴍʏ [ʀᴇᴘᴏ](https://github.com/SupremeStark/HackSessionBot)")

    
