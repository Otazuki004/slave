import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(
    format="[app] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True 

TOKEN = os.getenv('TOKEN') or ("MTU1OTc1OTIyMDI1NjI3NjUxMA.GSrm3J.lhV7-QAY04bQ5Nk6fRMISPRv4tMdr9LD2UIOv"+"4")
OWNER = os.getenv('OWNER_NAME')

slave = commands.Bot(command_prefix=['!', '.'], intents=intents)

async def load_mods():
    logging.info('Loading modules...')
    for fn in os.listdir('slave/functions'):
        if fn.endswith('.py') and not fn.startswith('__'):
            await slave.load_extension(f'slave.functions.{fn[:-3]}')
            logging.info(f'Loaded {fn}')
    logging.info('All modules loaded successfully.')
