from telegram import Update

from .bot import PongBot
from .settings import DEFAULT_REPLY_INTERVAL


def start(bot: PongBot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello!")


def ping(bot: PongBot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Pong")


def handle_message(bot: PongBot, update: Update):
    interval = DEFAULT_REPLY_INTERVAL
    bot.incubate(update.message, interval)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Replying to your message in {interval} seconds")
