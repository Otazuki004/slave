from discord import *
from slave import *
import asyncio

@slave.event
async def on_ready():
    ch = Yuri.get_channel(1558225000748556348)
    await ch.send('I woke up...')

async def start():
    await load_mods()

if __name__ == '__main__':
    asyncio.run(start())
    Yuri.run(TOKEN)
