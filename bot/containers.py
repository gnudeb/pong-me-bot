
class Message:
    def __init__(self, message_dict):
        if 'text' not in message_dict:
            raise NotImplementedError("Non-text messages are not implemented yet.")
        self.text = message_dict['text']
        self.author_id = message_dict['from']['id']


class Response:
    def __init__(self):
        pass
