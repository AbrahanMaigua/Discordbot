from datetime import datetime
import discord 
from discord.ext import commands


class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot 

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.guild)  
  async def help(self, ctx):
    embed = discord.Embed(title='Help!', describe='How to the commands!', Timestamp=datetime.utcnow(), colour=discord.Colour.blue())
    embed.add_field(name=f"$ping", value="This command is too show the latency of the bot", inline=True)
    embed.add_field(name=f"$purge", value=f"Syntax: $purge (amount of messages), This command is too delete certant amount of messages in a channel!", inline=True)
    embed.add_field(name=f"$img", value=f"Syntax: $img (type)(query) generate a random (you can write $img row and query all the allowed fields)", inline=True)
    
    #embed.add_field(name=f"$tempmute", value=f"Syntax: $tempmute (member) (time) (time delay(example: s, m, h, d)) (reason), This command is to temperaly mute a member!", inline=True)
    #embed.add_field(name=f"$mute", value=f"Syntax: $mute (member) (reason), This command is to permentaly mute a member untill unmuted with a command", inline=True)
    #embed.add_field(name=f"$unmute", value=f"Syntax: $unmute (member), This command is to unmute a member forcefully", inline=True)
    #embed.add_field(name=f"$kick", value=f"Syntax: $kick (member) (reason, This command is to kick a member from you're guild! They still can rejoin if given an invite)", inline=True)
    #embed.add_field(name=f"$tempban", value=f"Syntax: $tempban (member) (time) (time delay(example: s, m, h, d)) (reason), This command is to temperaly ban a member untill time is up or unban command is called on the member", inline=True)
    #embed.add_field(name=f"$ban", value=f"Syntax: $ban (member) (reason), This command is to permentaly mute a member untill unbannedd with a command", inline=True)
    #embed.add_field(name=f"$unban", value=f"Syntax: $unban (member), This command is to unban a member forcefully", inline=True)
   
    await ctx.reply(embed=embed)


def setup(bot):
  bot.add_cog(Help(bot))