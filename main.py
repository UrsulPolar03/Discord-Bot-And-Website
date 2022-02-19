import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import youtube_dl
from discord.utils import get
import asyncio
from keep_alive import keep_alive
from music import music_cog
import pafy
from discord.ext.commands import Bot
from history import *

client = discord.Client()
client = commands.Bot(command_prefix = '/')
  
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

@client.event 
async def on_ready():
  print("Bot-ul este ONLINE")
  await client.change_presence(status=discord.Status.online, activity=discord.Game("/ajutor"))

@client.command()
async def ajutor(ctx):
  await ctx.send("p, stop, site")

@client.command()
async def site(ctx):
  await ctx.send("https://spirit-box.ursulpolar03.repl.co/")

@client.command(pass_context = True)
async def join(ctx):
  if(ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("Nu esti conectat pe un canal voce.")

@client.command(pass_context = True)
async def p(ctx, url :str):
  global is_playing
  ydl_opts = {'format': 'bestaudio'}
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download = False)
    title = info.get("title", None)
    URL = info['formats'][0]['url']
  if(ctx.voice_client is None):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = discord.FFmpegPCMAudio(URL)
    player = voice.play(source)
    await ctx.send("**%s** a dat play la melodia : " %ctx.message.author.name + "**"+title+"**")
    statusu = convertTuple(title)
    print (statusu)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(statusu))
    final = convertTuple(title) + " " + "(" + ctx.message.author.name + ")" 
    addh(final)
  else:
    voice = ctx.guild.voice_client
    source = discord.FFmpegPCMAudio(URL)
    try:
      player = voice.play(source)
      await ctx.send("**%s** a dat play la melodia : " %ctx.message.author.name + "**"+title+"**")
      statusu = convertTuple(title)
      print (statusu)
      await client.change_presence(status=discord.Status.online, activity=discord.Game(statusu))
      final = convertTuple(title) + " " + "(" + ctx.message.author.name + ")" 
      addh(final)
    except:
      await ctx.send("Deja cant o melodie.")
  await ctx.message.delete()
  print (history)

@client.command(pass_context = True)
async def stop(ctx):
  voice = ctx.guild.voice_client
  voice.stop()
  await ctx.send("Am fost oprit de catre (**"+ctx.message.author.name+"**)")
  await ctx.message.delete()

@client.command(pass_context = True)
async def test(ctx):
  channel = ctx.message.author.voice.channel
  if(ctx.voice_client is None):
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio("song.mp3")
    player = voice.play(source)
  else:
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio("song.mp3")
    player = voice.play(source)  

keep_alive()
on_ready()
client.run("OTA2MTQyOTk3*CENSORED*Jo-QoncCBUeB_sYVXy1SGduVk")