from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
**ʜᴇʏ {},**
ɪ'ᴍ **{}** ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴜsᴇʀs ᴀᴄᴄᴏᴜɴᴛ.

ɪ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ
ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ I ᴄᴀɴ ᴅᴏ.
"""
HACK_TEXT = """
"A" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴏᴡɴ ɢʀᴏᴜᴘs ᴀɴᴅ ᴄʜᴀɴɴᴇʟs]
"B" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴀʟʟ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ʟɪᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, ᴜsʀɴᴀᴍᴇ... ᴇᴛᴄ]
"C" :~ [ʙᴀɴ ᴀ ɢʀᴏᴜᴘ {ɢɪᴠᴇ ᴍᴇ SᴛʀɪɴɢSᴇssɪᴏɴ ᴀɴᴅ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴜsᴇʀɴᴀᴍᴇ ɪ ᴡɪʟʟ ʙᴀɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴛʜᴇʀᴇ}]
"D" :~ [ᴋɴᴏᴡ ᴜsᴇʀ ʟᴀsᴛ ᴏᴛᴘ {𝟷sᴛ ᴜsᴇ ᴏᴘᴛɪᴏɴ B ᴛᴀᴋᴇ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴀɴᴅ ʟᴏɢɪɴ ᴛʜᴇʀᴇ Aᴄᴄᴏᴜɴᴛ ᴛʜᴇɴ ᴜsᴇ ᴍᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴏᴛᴘ}]
"E" :~ [Jᴏɪɴ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ SᴛʀɪɴɢSᴇssɪᴏɴ]
"F" :~ [Lᴇᴀᴠᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ ᴠɪᴀ SᴛʀɪɴɢSᴇssɪᴏɴ]
"G" :~ [Dᴇʟᴇᴛᴇ A Gʀᴏᴜᴘ/Cʜᴀɴɴᴇʟ]
"H" :~ [ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴛᴡᴏ sᴛᴇᴘ ɪs ᴇɴᴇᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ]
"I" :~ [ᴛᴇʀᴍɪɴᴀᴛᴇ Aʟʟ ᴄᴜʀʀᴇɴᴛ ᴀᴄᴛɪᴠᴇ sᴇssɪᴏɴs ᴇxᴄᴇᴘᴛ Yᴏᴜʀ SᴛʀɪɴɢSᴇssɪᴏɴ]
"J" :~ [ᴅᴇʟᴇᴛᴇ Aᴄᴄᴏᴜɴᴛ]
"K" :~ [ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"L" ~ [ᴅᴇᴍᴏᴛᴇ ᴀʟʟ ᴀᴅᴍɪɴs ɪɴ ᴀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ]
"M" ~ [ᴄʜᴀɴɢᴇ Pʜᴏɴᴇ ɴᴜᴍʙᴇʀ ᴜsɪɴɢ SᴛʀɪɴɢSᴇssɪᴏɴ]
"""


PM_BUTTON = IKM([[IKB("🤖 ʜᴀᴄᴋ", callback_data="hack_btn")]])

HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
        IKB("J", callback_data="J"),           
    ],
    [
        IKB("K", callback_data="F"),
        IKB("L", callback_data ="G"),
        IKB("M", callback_data="H"),                   
    ],
    ],    
    )



LOG_TEXT = "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●\n"
LOG_TEXT += "⊙ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\n"
LOG_TEXT += "⊙ ᴘʀᴏɪᴇᴄᴛ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ʜᴛᴛᴘs://ɢɪᴛʜᴜʙ.ᴄᴏᴍ/SᴜᴘʀᴇᴍᴇSᴛᴀʀᴋ\n\n"
LOG_TEXT += "⊙ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ:\n"
LOG_TEXT += "  @sᴛᴇᴠᴇ_ʀᴏɢᴇʀs_𝟷𝟶𝟷\n"
LOG_TEXT += "●▬▬▬▬▬▬▬▬▬▬▬▬๑۩ ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ۩๑▬▬▬▬▬▬▬▬▬▬▬●"
