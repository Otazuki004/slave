import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.default()
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


if __name__ == "__main__":
    main()
