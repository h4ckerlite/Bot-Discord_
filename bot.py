
import discord
from discord.ext import commands
from urllib import  parse, request
import  re
import datetime

bot = commands.Bot(command_prefix="!", description="¡Hola soy un bot de ayuda! Te puedo servir en algo")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")
@bot.command()
async def ip(ctx):
    await ctx.send("IP: Proximamente")

@bot.command()
async def estatus(ctx):
    await ctx.send("Status Server: En Mantenimiento")

@bot.command()
async def normas(ctx):
    await ctx.send("""
    ■ No hacer spam
    ■ No dejar links
    ■ No insultar
    ■ Y lo mas importante  divierte y pasa el rato
    """)

@bot.command()
async def suma(ctx, uno: int, dos: int):
    await ctx.send(uno + dos)

@bot.command()
async def resta(ctx, uno: int, dos: int):
    await ctx.send(uno - dos)

@bot.command()
async def times(ctx, uno: int, dos: int):
    await ctx.send(uno * dos)

@bot.command()
async def divide(ctx, uno: int, dos: int):
    await ctx.send(uno / dos)

#youtube
@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    #search_results #= re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
    #print(search_results)
    await ctx.send("https://www.youtube.com/watch?v=" + search_results[0])



#eventos
@bot.event
async def on_ready():
    print("El Bot esta listo para su uso!")

bot.run("ODkwNzI4NzgyMTA3OTEwMjE0.YU0B0g.wgo3fqKhhRSUVQb-dpvM8ZPc-Kc")