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

discussion = client.get_channel(1094398504635473930)
project_display = client.get_channel(1094444412773335140)
project_help = client.get_channel(1094444181730111618)

#overrides page formatting for MinimalHelpCommand -> puts each page in an embed
class MyNewHelp(commands.MinimalHelpCommand):
  async def send_pages(self):
    destination = self.get_destination()
    for page in self.paginator.pages:
      emby = discord.Embed(description=page)
      await destination.send(embed=emby)
client.help_command = MyNewHelp()

class MyHelp(commands.HelpCommand):
  async def send_bot_help(self, mapping):
    embed = discord.Embed(title="Help")
    for cog, commands in mapping.items():
      command_signatures = [self.get_command_signature(c) for c in commands]
      if command_signatures:
        cog_name = getattr(cog, "qualified_name", "No Category")
        #embed.add_field(name=cog_name, value)
    channel = self.get_destination()
    await channel.send(embed=embed)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#when a message is sent
@client.event
async def on_message(message):   
  if message.author == client.user:
    return 

  # process commands
  await client.process_commands(message)

@client.command()
async def welcomemessage(ctx):
  global discussion, project_display, project_help
  
  embed1 = discord.Embed()
  embed1.set_image(url=("https://i.imgur.com/W0RGFgt.png"))
  embed2 = discord.Embed(title="Welcome to the Scratch Olympiad Discord Server!", description="Starting 2017 Scratch Olympiad unites participants from all continents. Scratch is a visual event-driven programming environment designed for children and adolescents, while at the same time finding millions of adult fans. Scratch is the door to the world of \"big programming\" and the Scratch Olympiad brings together the most talented future developers and innovators.\n\nStudents from 7 years old and adults from any corner of the United States of America can become participants in the American national selection stage of the Scratch Olympiad.")
  embed3 = discord.Embed(title="Server Guidelines",description="Please read and adhere to the following rules so we can foster a supportive and friendly environment!")
  embed4 = discord.Embed(title="Rules",description="1. Be kind and inclusive towards other server members.\n\n2. Please message a moderator if you have a question, need help with anything, or notice someone breaking a server rule.\n\n3. Please keep topics of conversation within relevant channels.\n\n4. Follow the Discord Community Guidelines.\n\n5. Do not use any offensive or harmful language.\n\n6. Please use our "+discussion.name+" channel only for topics related to the Scratch Olympiad or STEM/Computer Science related questions.\n\n7. Our "+project_display.name+" channel and "+project_help.name+" channel are dedicated to questions related to Scratch Olympiad or other Computer Science projects you are working on.")
  await ctx.send(embeds = [embed1,embed2,embed3,embed4])
keep_alive()
client.run(token)