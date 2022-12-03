# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTAzODQ5NTQ5NzAzMzM1MTI3OQ.GDALvN.VWzvyDbh4ROWWu0oUjs6kOH3I9iKiY_MwVxXZg')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)
