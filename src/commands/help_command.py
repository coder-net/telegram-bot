import command_interface as commands


def help_command(message):
    return {
            'text': '\n'.join([c.description for c in commands.Command.commands_dict.values()]), 
#            'parse_mode': 'Markdown'
        }


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

