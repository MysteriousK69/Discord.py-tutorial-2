import discord # Import discord
from discord.ext import commands # from discord.ext import commands
from discord.ext.commands import bot # from discord.ext.commands import bot

bot = commands.Bot(ocmmand_prefix='!') # set your bots prefix

token = 'token here' # ADD YOUR BOTS TOKEN HERE

@bot.command(pass_context=True)
@commands.has_role("Admin") # add a role requirement to run the commmand
async def ban(ctx, content, member: discord.Member):
    try:
        await member.send(f"You were banned for {content}") # send a dm to the user informing that they were banned
        await member.ban() # ban a user
        await ctx.send("Successfully banned them") # send a msg in chat informing the admin that user was banned
    except:
        await ctx.send("You dont have perms to perform that action or you did not mentiona  valid user/did not give a valid reason") # send a error msg saying user was not banned
        await ctx.send("try doing it this way: !ban { member} {reason}") # give the right format for banning users

@bot.command(pass_context=True)
@commands.has_role("Admin") # add a role requirement to run the commmand
async def kick(ctx, content, member: discord.Member):
    try:
        await member.send(f"You were kicked for {content}") # send a dm to the user informing that they were kicked
        await member.kick() #kick a user
        await ctx.send("Successfully kicked them") # send a msg in chat informing the admin that suer was banned
    except:
        await ctx.send("You dont have perms to perform that action or you did not mention a valid user/did not give a valid reason") # send a error msg saying user was not kicked
        await ctx.send("try doing it this way: !kick { member} {reason}") # give the right format for kicking users


bot.run(token) # run the bot