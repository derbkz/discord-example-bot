import discord

bot_token = "TOKEN"
bot_intents = discord.Intents.default()
bot_client = discord.Client(intents=bot_intents)

@bot_client.event
async def on_ready():
    await bot_client.wait_until_ready()
    print("The bot is now ready")

# If a message is written, this event is triggered.
@bot_client.event
async def on_message(message):
   if message.author == bot_client.user:
        return
   await message.channel.send(f"{message.author} thank you for your message!") 

# If a reaction is added to a message, this event is triggered
@bot_client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f"{user} added a reaction.")

# If a message is edited, this event is triggered. 
@bot_client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'A message has been edited:\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )        

bot_client.run(bot_token)
