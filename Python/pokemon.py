import discord, basepoke
from discord.ext import commands
import asyncio
class Pokemon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(brief="muestra tu pokedex")
    async def pokedex(self, ctx):
        pokes = basepoke.pokdx(ctx.author.id)

        page1 = discord.Embed(title="Pokedex 1/6",description="```" + '\n'.join(pokes[:26]) + "```", colour=discord.Colour.orange())
        page2 = discord.Embed(title="Pokedex 2/6",description="```" + '\n'.join(pokes[26:50]) + "```", colour=discord.Colour.orange())
        page3 = discord.Embed(title="Pokedex 3/6",description="```" + '\n'.join(pokes[50:75]) + "```", colour=discord.Colour.orange())
        page4 = discord.Embed(title="Pokedex 4/6",description="```" + '\n'.join(pokes[75:100]) + "```", colour=discord.Colour.orange())
        page5 = discord.Embed(title="Pokedex 5/6", description="```" + '\n'.join(pokes[100:125]) + "```", colour=discord.Colour.orange())
        page6 = discord.Embed(title="Pokedex 6/6", description="```" + '\n'.join(pokes[125:]) + "```", colour=discord.Colour.orange())
        # un sistema de paginacion, no consegui hacer algo mas limpio
        # puedes conseguir la lista completa sin embed, retornando pokes
        poke_pages = [page1,page2,page3,page4,page5,page6]
        buttons = [u"\u2B05", u"\u27A1"]
        current = 0
        msg = await ctx.send(embed=poke_pages[current])

        for button in buttons:
            await msg.add_reaction(button)

        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction,user: user == ctx.author and reaction.emoji in buttons,timeout=60.0)

            except asyncio.TimeoutError:
                return print("acabo el tiempo de visualizacion de una pokedex")

            else:
                previous_page = current
                if reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1

                elif reaction.emoji == u"\u27A1":
                    if current < len(poke_pages) - 1:
                        current += 1


                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current != previous_page:
                    await msg.edit(embed=poke_pages[current])





async def setup(client):
    await client.add_cog(Pokemon(client))