import discord
from discord.ext import commands
import basepoke, asyncio, pokemon
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)




@bot.event
async def on_ready():
    print("ya desperte")
    cogs = [pokemon]
    for i in range(len(cogs)):
        await cogs[i].setup(bot)
    # puedes añadir tus cogs, aqui no importo basepoke.py como una cog
    # para que el usuario no pueda acceder a ella como comandos


    ctx = bot.get_channel(1124157632001884330)
    # el canal donde van a aparecer los pokemon

    def check(m):
        return m.content.lower() == "catch"

    while basepoke.activo == True:
        await asyncio.sleep(300)
        # tiempo de spawneo despues del catch
        # añadir un random
        # hola mundo
        poke = basepoke.spawneo()
        imag = "/home/roland/Escritorio/Discord Bot/poke/" + str(poke[0]) + ".png"
        file = discord.File(imag)
        await ctx.send("aparecio un: " + poke[1], file=file)
        try:
            atrapar = await bot.wait_for("message", check=check, timeout=180.0)
            # tiempo para que se escapen los pokemon en timeout
        except asyncio.TimeoutError:
            await ctx.send("se escapo tu " + poke[1])
        else:
            await ctx.send(str(atrapar.author) + " atrapaste un:" + poke[1])
            basepoke.registercatch(atrapar.author.id, poke[0])



@bot.command(brief="sale la pata de twinkle")
async def pata(ctx):
    await ctx.send("https://media.discordapp.net/attachments/824803074446983178/854126682230751272/Screenshot_20210614-173412.png?width=225&height=475")




bot.run("OTc1OTE2NjgwMTY3NDMyMjcy.Gwh--o.ICmpzogZD_apbZgTGXh5jBISYARI3C3V3NL-TY")