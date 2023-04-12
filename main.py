import os
import discord
from discord.ext import commands
from discord.utils import find
from replit import db
from keep_alive import keep_alive

token = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.reactions = True

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='&', help_command=commands.MinimalHelpCommand(), activity = discord.Game(name="&help"), intents=intents)
