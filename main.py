
import discord
from discord.ext import commands

TOKEN = 'PUT YOUR BOT TOKEN HERE'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='dmall')
@commands.has_permissions(administrator=True)
async def dm_all(ctx, *, message: str):
  
    if ctx.author == bot.user:
        return

    guild = ctx.guild
    members = guild.members

    for member in members:
        if not member.bot:
            try:
                await member.send(message)
                print(f"DM sent to {member.name}")
            except discord.Forbidden:
                print(f"Could not send DM to {member.name} (Forbidden)")
            except Exception as e:
                print(f"Error sending DM to {member.name}: {e}")

    await ctx.send("DMs have been sent to all members!")

@dm_all.error
async def dm_all_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    else:
        await ctx.send(f"An error occurred: {error}")

bot.run(TOKEN)
