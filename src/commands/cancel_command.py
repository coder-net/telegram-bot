import app
import command_interface as commands


def cancel_command(message):
    return {
        'text': 'Detele buttons',
        'reply_markup': {
            'remove_keyboard': True
        }
    }


commands.Command(
    '/cancel',
    cancel_command,
    '`/cancel` - remove keyboard buttons'
)
