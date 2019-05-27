commands_list = []


class Command:
    def __init__(self, keys, command, description=''):
        self._keys = keys
        self._description = description
        self.handle = command
        commands_list.append(self)

    @property
    def keys(self):
        return self._keys

    @property
    def description(self):
        return self._description

