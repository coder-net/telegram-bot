import command_interface as commands


def help_command(message):
    result = ''
    for command in commands.commands_list:
        result += '{}\n'.format(command.description)
    return result


commands.Command(
    [r'/help\s*', r'/start\s*'],
    help_command,
    '/help - get help'
)

