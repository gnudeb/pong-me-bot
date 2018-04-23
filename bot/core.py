from telepot import Bot as BaseBot
from telepot.loop import MessageLoop
from .settings import TG_TOKEN
from .rules import ruleset


class Bot(BaseBot):
    """Wrapper around `telepot`'s Bot. Inits with `TG_TOKEN` taken from settings.py."""
    def __init__(self, token=TG_TOKEN):
        super().__init__(token)

    def run(self):
        """Set up a message handler and start message polling"""
        handler = MessageHandler(
            rules=ruleset,
            default_handle=lambda msg: "404",
        )
        MessageLoop(self, handler).run_forever()


class MessageHandler:
    """Stores and returns handles that match a given text."""
    def __init__(self, rules=None, default_handle=None):
        self.rules = rules or {}
        self.default_handle = default_handle

    def __call__(self, message):
        return self.get_handle(message)

    def get_handle(self, message):
        """
        Match `message` to rules in `self.rules` and return a
        corresponding handle if match was made. Otherwise return
        `self.default_handle`.
        """
        for rule, handle in self.rules.items():
            if self.match(rule, message):
                return handle
        return self.default_handle

    @staticmethod
    def match(rule, message):
        """
        Check if a message matches to a rule and return `bool`.

        This method is implemented separately to provide a capability to
        match messages to complex conditional rules (e.g. regex).
        """
        return rule is message
