import discord
from discord.ext import commands
import json
import requests
from config import settings

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True

bot = commands.Bot(command_prefix = settings['prefix'], intents=intents) # Так как мы указали префикс в settings, обращаемся к словарю с ключом prefix.

# С помощью декоратора создаём первую команду
@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

bot.run('token')