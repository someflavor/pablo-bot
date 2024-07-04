import discord
from discord.ext import commands
import openai
import logging
import time

# initialize logging
logging.basicConfig(level=logging.INFO)

# api
DISCORD_TOKEN = 'HERE'
OPENAI_API_KEY = 'HERE'

# open ai key var
openai.api_key = OPENAI_API_KEY

#prefix is just the command input
prefix = input("Enter your bot's prefix bitch: ")
intents = discord.Intents.all()

#the bot instance
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

@bot.event
async def on_ready():
    logging.info(f'Shit is ready. Logged in as {bot.user}')

@bot.command(name='chat')
async def chat(ctx, *, message: str):
    try:
        # Use OpenAI to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=150
        )
        answer = response.choices[0].text.strip()
        await ctx.send(answer)
    except Exception as e:
        logging.error(f'Error: {e}')
        await ctx.send(f'Error: {e}')

bot.run(DISCORD_TOKEN)
