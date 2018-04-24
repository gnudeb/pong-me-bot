from .containers import Message
from .rules import ruleset


class MessageHandler:
    """Stores and returns handles that match a given message_dict."""
    def __init__(self, rules=None, default_handle=None):
        self.rules = rules or ruleset
        self.default_handle = default_handle

    def __call__(self, message_dict):
        message = Message(message_dict)
        handle = self.get_handle(message.text)
        handle(message)

    def get_handle(self, text):
        """
        Match `text` to rules in `self.rules` and return a
        corresponding handle if match was made. Otherwise return
        `self.default_handle`.
        """
        for rule, handle in self.rules.items():
            if self.match(rule, text):
                return handle
        return self.default_handle

    @staticmethod
    def match(rule, text):
        """
        Check if a message matches to a rule and return `bool`.

        This method is implemented separately to provide a capability
        to override this method to support complex conditional rules
        (e.g. regex).
        """
        return rule == text
