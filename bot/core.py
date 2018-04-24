from telepot import Bot as BaseBot
from telepot.loop import MessageLoop
from .settings import TG_TOKEN
from .message_handler import MessageHandler


class Bot(BaseBot):
    """Wrapper around `telepot`'s Bot. Inits with `TG_TOKEN` taken from settings.py."""
    def __init__(self, token=TG_TOKEN, handler=None):
        super().__init__(token)
        self.handler = handler

    def run(self):
        """Set up a message handler and start message polling"""
        handler = MessageHandler()
        MessageLoop(self, self.handler).run_forever()
