import discord
from discord.ext import commands
import os
import random
from replit import db
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "!")
@client.event
async def on_ready():
  print("bot is ready")

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def pong(ctx,):
  await ctx.send("It's '!ping', Not '!pong'!")

@client.command(aliases = ["8ball"])
async def _8ball(ctx,*,Question):
  Responds = ["try again", "ya!", "nu!"]
  await ctx.send(f'Question: {Question}\nAnwser: {random.choice(Responds)}')

keep_alive()
client.run(os.getenv('TOKEN'))