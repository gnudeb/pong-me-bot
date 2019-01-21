from telegram import Message, Bot

from .incubator import Incubator


class PongBot(Bot):
    def __init__(self, token, reply_interval):
        super().__init__(token=token)

        self.reply_interval = reply_interval
        self._incubator: Incubator = Incubator()

    def incubate(self, message: Message, interval: int=None):
        interval = interval or self.reply_interval
        self._incubator.add(message, interval)

    def dispatch_ready_messages(self, job):
        for message in self._incubator.pop_ready():
            message.forward(message.chat_id)
