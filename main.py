import discord
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
 
    if message.content.startswith('hi'):
        await message.channel.send('Hello!')

 
client.run('MTA0ODgxNjc3NTkyNTYxMjU5NA.G4uxy_.W5WV13nN0ZyuETrqDLW8BJcRCDubGfzAErwH9Y')
