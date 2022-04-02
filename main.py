import discord
from discord.ext import commands
import youtube_dl
from os import remove
from dotenv import dotenv_values

TOKEN = dotenv_values(".env")["BOT_TOKEN"]

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='>', intents=intents)

CHANNEL_ID = dotenv_values(".env")["CHANNEL_ID"]

@bot.event
async def on_message(ctx):
    if ctx.channel.id != int(CHANNEL_ID) or ctx.author.bot == True or "https://" not in ctx.content:
        return
    links = ctx.content.replace("\n"," ").split(" ")
    for link in links:
        print(link)
        id = link.split("/")[-1]
        ydl_opts = {'outtmpl': f'/output/{id}.mp4'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("downloaded")
        await ctx.channel.send(f"Bee...Bee...\nDownloaded attachment from <{link}>",file=discord.File(f"./output/{id}.mp4"))
        remove(f"./output/{id}.mp4")
        print("next")
    
bot.run(TOKEN)