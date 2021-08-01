import discord
from discord import channel
from discord import guild
from discord.ext import commands
from discord import Intents
import asyncio
import json,os
import requests
import random
from random import choice

intents = Intents.default()
intents.members = True
image = [
  'https://images.news18.com/ibnlive/uploads/2020/12/1608629135_untitled-design-3.png',
'https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg',

'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDM5IJt5ypTvJMC5zLyoTSCdneVIrp1VpHSQ&usqp=CAU',
'<https://www.youtube.com/watch?viik25wqIuFo>'

]
os.chdir("C:\\Users\\akdro\\OneDrive\\Desktop\\Progaming\\Python\\newbot.py")

client = commands.Bot(command_prefix="#",intents=intents)
client.remove_command("help")


@client.event
async def on_ready():
    print("{0.user} is online".format(client))
    channel_id = client.get_channel(772475290541752354)
    await channel_id.send("{0.user} is online".format(client))

@client.event
async def on_member_join(member):
 channel = discord.utils.get(member.guild.channels,name="general")
 if not channel:
   channel = guild.create_channel(name="general")
 await channel.send(f"hi {member.mention} hope u like this server  ")



@client.event
async def on_member_remove(member):
   channel = discord.utils.get(member.guild.channels,name="general")
   await channel.send(f"hi {member.mention} hope u like this server and remember us plz  ")
   await member.send(f"hi {member.mention} hope u like this server and remember us plz")
@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id ==  871011930679169024:
    guild_id = payload.guild_id
    guild = discord.utils.find()

@client.command()
async def ping(ctx):
  await ctx.send(f":ping_pong: Pong{round(client.latency * 1000)} ms")
@client.command()
async def confirm(ctx,member:discord.Member):

  memberrole = discord.utils.get(ctx.guild.roles,name="Member") 
  
  if not memberrole:
    memberrole = await ctx.guild.create_role(name="Member")

  await member.add_roles(memberrole)

  await ctx.send(f"Thnx for confirming urself {member.mention}")
  await member.send(f"you are now a verified member{member.mention}")

@client.command()
async def kick(ctx, member:discord.Member,*,reason=None):
  await member.send(f"you were kicked from {ctx.guild.name} because {reason} {member.mention} ")
  await member.kick(reason=reason)
  await ctx.send(f"{member.mention} has been kicked because {reason} ")
@client.command()
async def ban(ctx, member:discord.Member,*,reason=None):
  await member.send(f"you were kicked from {ctx.guild.name} because {reason} {member.mention} ")
  await member.ban(reason=reason)
  await ctx.send(f"{member.mention} has been kicked because {reason} ")



@client.command()
async def mute(ctx,member:discord.Member,*,reason=None):
  guild = ctx.guild
  mutedRole =discord.utils.get(guild.roles,name="Muted")
  if not mutedRole:
    mutedRole  = await guild.create_role(name="Muted")

    for channel in guild.channels:
      await channel.set_permissions(mutedRole,speak=False,send_messages=False,read_message_history=False,read_messages=False) 
  await member.add_roles(mutedRole,reason=reason)
  await ctx.send(f"{member.mention} has muted for reason {reason}")
  await member.send(f"You have been muted in {guild.name} for {reason}")
@client.command()
async def unmute(ctx,member:discord.Member):
  mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")
  await member.remove_roles(mutedRole)
  await ctx.send(f"Unmuted {member.mention}")
  await member.send(f"You were muted from the server {ctx.guild.name} ")

@client.command()
async def alive(ctx,member:discord.Member):
  mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")
  await member.remove_roles(mutedRole)
  await ctx.send(f"Unmuted {member.mention}")
  await member.send(f"You were muted from the server {ctx.guild.name} ")

@client.command()
async def userinfo(ctx,user:discord.Member):
  await ctx.send(user.id) 

@client.command()
async def roleinfo(ctx,role:discord.Role):
  await ctx.send(role.id)


@client.command()
async def multinfo(ctx,user:discord.Member,role:discord.Member):
  await ctx.send(user.id)
  await ctx.send(role.id)

@client.command(name="_8ball",aliases=['8ball','test'])
async def _8ball(ctx,*,question):
    responses = [
              "It is Certain.",
             'It is decidedly so.',
             'Without a doubt.',
             'Yes definitely.',
             'You may rely on it.',
             'As I see it, yes.',
             'Most likely.',
             'Outlook good.',
             'Yes.',
             'Signs point to yes.',

             'Reply hazy, try again.',
             'Ask again later.',
             'Better not tell you now.',
             'Cannot predict now.',
             'Concentrate and ask again.',
             "Don't count on it.",
             'My reply is no.',
             'My sources say no.',
             'Outlook not so good.',
             'Very doubtful.']


    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')
@client.command(aliases = ["av","Avatar"])
async def avatar(ctx,member:discord.Member =None):
  if member  == None :
    member = ctx.author
  memberav = member.avatar_url
  em =  discord.Embed(
    title = f"{member.name}'s avatar",
  )
  em.set_image(url = memberav)
  await ctx.send(embed=em)


@client.command()
@commands.has_permissions(manage_messages=True)
async def unban(ctx,*,member):

  banned_users = ctx.guild.bans()
  member_name, member_discriminator= member.split("#")


  for ban_entry in banned_users:
    user = ban_entry.user


    if (user.name,user.discriminator)  == (member_name,member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'unbanned {user.mention}')
      return


@client.command()
async def sus(ctx):
  await ctx.send(random.choice(image))
@client.command()
async def clear(ctx,amount:int):
  await ctx.channel.purge(limit=amount)  
@client.command()  
async def help(ctx):
  em = discord.Embed(
    title = "Help",
    description = f"``{ctx.author.name}`` asked for help for command ``{client.user}``",
    color = discord.Color.blue())
  em.add_field(name="ping",value =":ping_pong: Pong!",inline=True)
  em.add_field(name="memberav",value ="gives out member avatar",inline=False)
  await ctx.send(embed=em)  











client.run("ODY0NjgxODgzMTQ4ODc3ODU1.YO4_wQ.K-kQqffCk2nvfEleDgkBDl_IenA")








