commands_list = []


class Command:
    def __init__(self):
        self._keys = []
        self._description = ''
        commands_list.append(self)

    @property
    def keys(self):
        return self._keys

    @keys.setter
    def keys(self, keys):
        self._keys = keys

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    def handle(self, message):
        pass



