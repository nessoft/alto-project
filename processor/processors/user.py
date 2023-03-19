from processor.factories.user import UserRegister


class User:

    def __init__(self, action):
        self.action = action

    def register(self, msg):
        return UserRegister().process(msg)

    def start(self, msg):
        mapping = {
            'register': self.register
        }
        return mapping[self.action](msg)

