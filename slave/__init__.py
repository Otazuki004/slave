import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(
    format="[Yuri] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True 

TOKEN = os.getenv('TOKEN')
OWNER = os.getenv('OWNER_NAME')

slave = commands.Bot(command_prefix=['!', '.'], intents=intents)

async def load_mods():
    logging.info('Loading modules...')
    for fn in os.listdir('Yuri/functions'):
        if fn.endswith('.py') and not fn.startswith('__'):
            await Yuri.load_extension(f'Yuri.functions.{fn[:-3]}')
            logging.info(f'Loaded {fn}')
    logging.info('All modules loaded successfully.')
