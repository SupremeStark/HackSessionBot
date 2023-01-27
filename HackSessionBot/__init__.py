import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from motor.motor_asyncio import AsyncIOMotorClient
from HackSessionBot.Helpers.data import LOG_TEXT
from pyromod import listen 

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
OWNER_ID = Config.OWNER_ID
START_PIC = Config.START_PIC
CHAT = Config.CHAT
MONGO_DB = Config.MONGO_DB_URL

if not START_PIC:
    START_PIC = "https://graph.org/file/864483e9fb1cec38b67fe.jpg"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    
#db
if MONGO_DB:
        mongo = AsyncIOMotorClient(MONGO_DB)
        db = mongo.BSDK
else:
db = None 

async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    if db != None:
        LOG.print("[bold cyan]ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ᴍᴏɴɢᴏ ᴅʙ ᴜʀʟ ɴᴏᴡ ʏᴏᴜ ᴜsᴇ ɪᴛ ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ.")
    else:
        LOG.print("[bold red]ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴀᴅᴅᴇᴅ ᴀ ᴍᴏɴɢᴏ ᴜʀʟ Sᴏ ᴛʜᴇ ʙᴏᴛ ᴡɪʟʟ ᴡᴏʀᴋ ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴏᴅᴜʟᴇ")
    LOG.print("[bold yellow]sᴛᴀʀᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ɴᴏᴡ.......")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(HackSessionBot())    



    
    

    
    



