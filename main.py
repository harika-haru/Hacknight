# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTAzODQ5NTQ5NzAzMzM1MTI3OQ.G18GDv.mb0F3K1IRSdYhg7uSyRdKhLujGRQJeFuFZDvgw')

class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)