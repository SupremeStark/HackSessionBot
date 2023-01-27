import asyncio
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from motor.motor_asyncio import AsyncIOMotorClient
from MassActionBot.utils.data import LOG_MSG as START_TEXT

#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
SUDOES = Config.BAN_PROTECTED
OWNER_ID = Config.OWNER_ID
START_PIC = Config.START_PIC
MONGO_DB = Config.MONGO_DB_URL

if not START_PIC:
    START_PIC = "https://graph.org/file/c1c19fee2ac7b458087f7.jpg"

#rich
LOG = Console()


#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    



async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(START_TEXT)
    LOG.print(header)
    if MONGO_DB:
        mongo = AsyncIOMotorClient(MONGO_DB)
        db = mongo.AMSTARK
    LOG.print("[bold yellow]ɢᴇᴛᴛɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴛʜᴇ ʙᴏᴛ.....")
    await app.start()    
    LOG.print("[bold yellow]ɢᴏᴛ ᴀʟʟ ᴛʜᴇ ɪɴғᴏ......")
    await asyncio.sleep(0.5)
    


loop = asyncio.get_event_loop()
loop.run_until_complete(HackSessionBot())    



    
    

    
    



