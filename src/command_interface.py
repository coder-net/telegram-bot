class Command:
    commands_dict = {}

    def __init__(self, key, command, description=''):
        self._description = description
        self.handle = command
        Command.commands_dict[key] = self

    @property
    def description(self):
        return self._description

