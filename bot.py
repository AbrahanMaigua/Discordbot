from datetime import datetime
import discord, os
from discord.ext import commands
from dotenv import load_dotenv
#from comads import *

load_dotenv()
# prefix !
TOKEN =  os.getenv('DISCORD_TOKEN')
bot = commands.Bot('$')
bot.remove_command('help')
#commands.AutoShardedBot()

# All the events must be a coroutine. If they aren’t, 
# then you might get unexpected errors. In 
# order to turn a function into a coroutine they must 
# be async def functions.
# events are asynchronous functions@bot.event
@bot.event
async def on_ready():
  """
  Called when the client is done preparing the data
  received from Discord. Usually after login is
  successful and the Client.guilds and co. are filled up.

  """
  for filename in os.listdir(os.getcwd() + r'\Techer_bot\files\cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f"cogs.{filename[:-3]}")

  await bot.change_presence(activity=discord.Game("$help"))
  print("READY!")
 #  await bot.change_presence(status=discord.Status, activity=activity)
@bot.event
async def on_member_join(menber):
  await menber.create_dm()
  await menber.dm_channel.send(
    F'hi! your welcome {menber.name}, to my discord server!'
  )



bot.run(TOKEN)
