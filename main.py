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
async def rulesmessage(ctx):
  image = discord.Embed(color=discord.Color.from_rgb(255,255,255))
  image.set_image(url=("https://i.imgur.com/W0RGFgt.png"))
  welcome = discord.Embed(title="Welcome to the Scratch Olympiad Discord Server!", description="Since 2017, Scratch Olympiad has united participants from all continents. Scratch is a visual event-driven programming environment designed for children and adolescents, while at the same time finding millions of adult fans. Scratch is the door to the world of \"big programming\" and the Scratch Olympiad brings together the most talented future developers and innovators.\n\nStudents from 7 years old and adults from any corner of the United States of America can become participants in the American national selection stage of the Scratch Olympiad.", color=discord.Color.from_rgb(236,172,28))
  guidelines = discord.Embed(title="Server Guidelines",description="Please read and adhere to the following rules so we can foster a supportive and friendly environment!",color=discord.Color.from_rgb(4,116,187))
  rules = discord.Embed(title="Rules",description="1. Be kind and inclusive towards other server members.\n\n2. Please message a moderator if you have a question, need help with anything, or notice someone breaking a server rule.\n\n3. Please keep topics of conversation within relevant channels.\n\n4. Follow the Discord Community Guidelines which can be found [here](https://discord.com/guidelines).\n\n5. Do not use any offensive or harmful language.\n\n6. Please use our <#1094398504635473930> channel only for topics related to the Scratch Olympiad or STEM/Computer Science related questions.\n\n7. Our <#1094444412773335140> channel and <#1094444181730111618> channel are dedicated to questions related to Scratch Olympiad or other Computer Science projects you are working on.",color=discord.Color.from_rgb(107,171,36))
  await ctx.send(embeds = [image,welcome,guidelines,rules])

@client.command()
async def chaptermessage(ctx):
  welcome = discord.Embed(title="Welcome to the Scratch Olympiad Discord Server!", description="This chat is meant for communication with state representatives throughout the US to ensure the success of this program. ",color=discord.Color.from_rgb(255,255,255))
  thanks = discord.Embed(title="Thank you for accepting our offer!", description="Thank you so much to all the state representatives that have joined to help plan this to help grow STEM in all aspects! We, Plano West Robotics, thank you for your contribution to this competition.", color=discord.Color.from_rgb(61,61,109))
  info = discord.Embed(title="Extra Information",description="Please rename yourself to help everyone address each other better in this format: \n\nFIRST_NAME LAST_INITIAL | STATE ABBREVIATION\nEx: Akhil K | TX",color=discord.Color.from_rgb(180,36,52))
  await ctx.send("<@&1096639793510756384>",embeds = [welcome,thanks,info])

keep_alive()
client.run(token)