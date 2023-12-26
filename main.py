import discord
from openai import OpenAI
from config import DISCORD_TOKEN, OPENAI_API_KEY

# load OpenAI key
openai_client = OpenAI(
    api_key = OPENAI_API_KEY
)


# declare intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Initialize Discord client with specified intents
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    try:
        chat_completion = openai_client.chat.completions.create(
            messages=[{"role": "user", "content": message.content[5:]}],
            model="gpt-3.5-turbo",
        )
        await message.channel.send(chat_completion.choices[0].message.content)
    except Exception as e:
        await message.channel.send(f"An error occured: {e}")

client.run(DISCORD_TOKEN)