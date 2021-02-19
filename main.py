from discord.ext import commands
import os
import random
from keep_alive import keep_alive
client = commands.Bot(command_prefix="!")


@client.event
async def on_command_error(ctx, error):
    if hasattr(ctx.command, commands.MissingRequiredArgument):
      print("error handled")
    else:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Hey, That command doesn't exist.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Hey, I need you to input required arguments")
        else:
            await ctx.send(error)
        print(f"There was an error:\n{error}")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def pong(ctx):
    await ctx.send("It's '!ping', Not '!pong'!")


@client.command(name="8ball")
async def _8ball(ctx, *, Question):
    Responds = ["try again", "ya!", "nu!"]
    await ctx.send(f'Question: {Question}\nAnwser: {random.choice(Responds)}')


@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please input a question.")


keep_alive()
client.run(os.getenv('TOKEN'))
