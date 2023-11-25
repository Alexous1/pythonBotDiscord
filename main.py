import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix="/", intents=intents)

status = ['online', 'offline', 'idle', 'dnd', 'invisible']

load_dotenv(dotenv_path="config")

@bot.event
async def on_ready():
    print("Le bot est connecté.")

@bot.event
async def on_member_join(member):
    print(f"Un nouveau membre est arrivé : {member.display_name}")
    print("test")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user = await bot.fetch_user(payload.user_id)
    send_channel = await bot.fetch_channel()

    await send_channel.send(f"{user.display_name} a réagi à  \"{message.content}\" par {payload.emoji}")

@bot.command(name="del")
async def delete(ctx, number: int):
    messages = [message async for message in ctx.channel.history(limit=number + 1)]

    for each_message in messages:
        await each_message.delete()

@bot.command(name="clear")
async def clear(ctx):
    messages = [message async for message in ctx.channel.history(limit=None)]

    for each_message in messages:
        await each_message.delete()

@bot.command(name="send")
async def message_count(ctx):

    user = ctx.author
    total_count = 0
    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=None):
            if message.author == user:
                total_count += 1

    await ctx.send(f"{user.display_name} a envoyé un total de {total_count} messages sur ce serveur.")

@bot.command(name="BotStatus")
async  def bot_status(ctx, nb: int):

    print(nb)
    game = discord.Game("test")
    await bot.change_presence(status=status[nb], activity=game)

@bot.command(name="UserInfo")
async def user_info(ctx):

    user = ctx.author
    nb_message = 0
    print(user.id)
    print(nb_message)

    member = ctx.guild.get_member(user.id)

    channel = await bot.fetch_channel()

    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=None):
            if message.author == user:
                nb_message += 1

    await channel.send(
        f"{user.display_name} a envoyé {nb_message} messages dans ce serveur.")





bot.run(os.getenv("TOKEN"))