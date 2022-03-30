import discord
from discord.ext import commands
import aiohttp


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(name='img' )
    async def dog(self, ctx, endpoints, index: str = 'dog'):
        message = ctx.message

        print(message)
        await message.delete()
       
        endpo = {
              "Animal" : ['Dog', 'Cat', 'Panda',
               'Fox', 'Red panda', 'Koala',
             'Bird', 'Raccoon', 'Kangaroo', 'duck'],
             

             'Anime':['Wink', 'Pat', 'Hug'],
             
            }             
            
            
        embed = discord.Embed(title='list Endpoind', color=discord.Color.purple())
        embed = discord.Embed(name='Syntax', value='write endpoints in lowercase and replace spaces with **_**')

        for k in endpo.keys():
            v = ''

            for i in endpo[k]:
                
                v += f'{i}\n'

            embed.add_field(name=str(k), value=v)


        
        if endpoints == 'row':
        
            await ctx.send(embed=embed)
                

        else: 
             


            async with aiohttp.ClientSession() as session:
                try:
                
                    if endpoints == "anime":
                        requet  = await session.get(f'https://some-random-api.ml/animu/{index}')
                    elif index == "duck":
                        requet  = await session.get(f'https://random-d.uk/api/v2/random')
                    else:
                        requet  = await session.get(f'https://some-random-api.ml/{endpoints}/{index}')

                    dogjson = await requet.json() 
                except aiohttp.client_exceptions.ContentTypeError as e:
                   return await ctx.send(f"😔 Error: $img **{endpoints} {index}** can you write **$img row** you can write $img row and check all the allowed commands" )


            print(dogjson)
            if endpoints == "anime":
                embed = discord.Embed(title='Anime', color=discord.Color.purple())
                embed.set_image(url=dogjson['link'])
            elif index  == "duck":
                embed = discord.Embed(title=dogjson['message'], color=discord.Color.purple())
                embed.set_image(url=dogjson['url'])


            else:    
                embed = discord.Embed(title=dogjson['fact'], color=discord.Color.purple())
                embed.set_image(url=dogjson['image'])

            await ctx.send(embed=embed)

    



def setup(client):
    client.add_cog(Fun(client))