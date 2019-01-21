from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters

from .bot import PongBot
from .settings import TG_TOKEN
from . import handlers


class App:

    def __init__(self):
        self.bot = PongBot(TG_TOKEN)
        self.updater = Updater(bot=self.bot)

    def start(self):
        self._add_handlers()
        self._add_jobs()
        self.updater.start_polling()

    def _add_handlers(self):
        handlers_ = [
            CommandHandler("start", handlers.start),
            CommandHandler("ping", handlers.ping),
            MessageHandler(Filters.all, handlers.handle_message)
        ]

        for handler in handlers_:
            self.updater.dispatcher.add_handler(handler)

    def _add_jobs(self):
        self.updater.job_queue.run_repeating(
            callback=PongBot.dispatch_ready_messages,
            interval=1
        )
