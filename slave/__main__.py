import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
command_prefix="!",
intents=intents
)

@bot.event
async def on_ready():
print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
await ctx.send("I'm punisher's slave!")

def main():
import config
bot.run(config.TOKEN)

if name == "main":
main()
