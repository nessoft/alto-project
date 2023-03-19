
class Task:

    def __init__(self, action):
        self.action = action

    def create(self, msg):
        pass

    def edit(self, msg):
        pass

    def delete(self, msg):
        pass

    def start(self, msg):
        mapping = {
            'create': self.create,
            'edit': self.edit,
            'delete': self.delete
        }
        return mapping[self.action](msg)

