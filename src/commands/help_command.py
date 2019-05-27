import command_interface as commands


def help_command(message):
    result = ''
    for command in commands.Command.commands_dict.values():
        result += '{}\n'.format(command.description)
    return {'text':result}


commands.Command(
    '/help',
    help_command,
    '/help - get help'
)
commands.Command(
    '/start',
    help_command,
    '/start - start bot'
)

