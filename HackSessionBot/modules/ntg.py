import os
import random 
from HackSessionBot import app,LOG
from pyrogram import filters
from PIL import Image,ImageDraw,ImageFont


async def infopic(pic,id,user_name):
    img1 = Image.open("./HackSessionBot/modules/anya.jpg")
    img2 = Image.open(pic)   
    i_width, i_height = img1.size
    m_font = ImageFont.truetype("./HackSessionBot/modules/a.otf", int((70 / 640) * i_width)) 
    a = img2.resize((310,310))
    back_im = img1.copy()
    back_im.paste(a, (90, 50))                
    back_im.save(f"./HackSessionBot/modules/anya{id}.jpg")
    return f"./HackSessionBot/modules/anya{id}.jpg"
    

@app.on_message(filters.command("info"))
async def _ok(app, message):
    if message.sender_chat:
        return
    msg = await message.reply("`ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴜɴᴛʏ.......`")
    text = "╔──── ¤ ◎ ᴜsᴇʀ ɪɴғᴏ ◎ ¤\n"
    user = message.from_user
    
    text += f"\n **◎ ʏᴏᴜʀ ɪᴅ :** `{user.id}`"    
    if user.first_name :
        text += f"\n **◎ ғɪʀsᴛ ɴᴀᴍᴇ :** {user.first_name}"
    if user.last_name :
        text += f"\n **◎ ʟᴀsᴛ ɴᴀᴍᴇ :** {user.last_name}"
    if user.username :
        text += f"\n **◎ ᴜsᴇʀɴᴀᴍᴇ :** @{user.username}"
    text += f"\n **◎ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ :** {user.mention}" 
    
    text += f"\n **◎ ᴘʀᴇᴍɪᴜᴍ ᴜsᴇʀ :** `{user.is_premium}`"
    text += "\n\n╚──── ¤ ◎ ᴜsᴇʀ ɪɴғᴏ ◎ ¤"       
    
    
    try:
        pic = await app.download_media(user.photo.big_file_id, file_name=f"pp{message.from_user.id}.png")
    except AttributeError:
        pic = "./HackSessionBot/modules/anya.jpg"
    
    welpic = await infopic(pic,user.id,user.first_name)
    await msg.edit("`ᴀʟᴍᴏsᴛ ᴅᴏɴᴇ......`")
    
    await message.reply_photo(welpic, caption=text)
    await msg.delete()
    try:
        os.remove(welpic)
        if user.photo:
            os.remove(pic)
    except Exception as er:
        LOG.print(f"[bold red] {er}")
