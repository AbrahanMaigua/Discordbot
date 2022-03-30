import discord
import datetime
from discord.ext import commands

class AdminCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(colour=discord.Colour.green(), description=f"Welcome **{member.name}** Dev to my discord remember to check the rules channel. ")

        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_footer(text=member.guild, icon_url=member.guild.icon_url)
        embed.timestamp = datetime.datetime.utcnow()

        channel = self.client.channel()
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(AdminCommands(client))
