from datetime import datetime, timedelta
from typing import Set

from telegram import Message


class QueuedMessage:
    def __init__(self, message: Message, due_to: datetime):
        self.message = message
        self.due_to = due_to

    @staticmethod
    def from_interval(message: Message, interval: int):
        return QueuedMessage(
            message,
            datetime.now() + timedelta(seconds=interval)
        )

    def is_ready(self):
        return datetime.now() >= self.due_to


class Incubator:
    def __init__(self):
        self._messages: Set[QueuedMessage] = set()

    def add(self, message, interval):
        self._messages.add(QueuedMessage.from_interval(message, interval))

    def pop_ready(self):
        for message in self._messages.copy():
            if message.is_ready():
                yield message.message
                self._messages.remove(message)
