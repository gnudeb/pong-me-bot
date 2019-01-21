import json

from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters

from .bot import PongBot
from . import handlers


class App:

    def __init__(self, settings_path: str="default_config.json"):
        with open(settings_path, 'r') as f:
            self.settings = json.load(f)

        self.dispatch_interval = self.settings["DISPATCH_INTERVAL"]
        self.bot = PongBot(
            token=self.settings["TG_TOKEN"],
            reply_interval=self.settings["DEFAULT_REPLY_INTERVAL"])
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
            interval=self.dispatch_interval
        )
