import command_interface as commands


def help_command(message):
    result = ''
    for command in commands.commands_list:
        result += '{}: {}\n'.format(command.keys[-1], command.description)
    return result


help = commands.Command()
help.description = 'get help'
help.keys = [r'/help\s*', r'/start\s*']
help.handle = help_command

