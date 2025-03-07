import os
import discord
import ezcord
import yaml
from dotenv import load_dotenv

status = discord.Status.dnd
activity = discord.CustomActivity(name="Status")


bot = ezcord.Bot(
    intents=discord.Intents.all(),
    cache_app_emojis=True,
    command_prefix="!",
    activity=activity,
    status=status,
)

if __name__ == "__main__":
    bot.load_cogs("cogs", subdirectories=True)
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
