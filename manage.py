from bot.bot import Bot
from bot.settings import TG_TOKEN


async def echo(message):
    print(message['message']['text'])

bot = Bot(TG_TOKEN)
bot.handler = echo
bot.run()
