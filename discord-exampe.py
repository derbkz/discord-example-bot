import discord

bot_token = 'TOKEN'
bot_intents = discord.Intents.default()
bot_client = discord.Client(intents=bot_intents)

@bot_client.event
async def on_ready():
    await bot_client.wait_until_ready()

@bot_client.event
async def on_message(message):
   if message.author == bot_client.user:
        return
   await message.channel.send(f"{message.author} thank you for your message!") 

@bot_client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f"{user} added a reaction.")

bot_client.run(bot_token)