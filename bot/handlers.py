from telegram import Update

from .bot import PongBot


def start(bot: PongBot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello!")


def ping(bot: PongBot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text="Pong")


def handle_message(bot: PongBot, update: Update):
    bot.incubate(update.message)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Replying to your message in {bot.reply_interval} seconds")
