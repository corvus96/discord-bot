import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient()
client.run(os.getenv('TOKEN')) # Replace with your own token.