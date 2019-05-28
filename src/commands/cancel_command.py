import app
import command_interface as commands


def cancel_command(message):
    return {
        'text': 'Cancellation',
        'reply_markup': {
            'remove_keyboard': True
        }
    }


commands.Command(
    '/cancel',
    cancel_command,
    '/cancel - remove keyboard buttons'
)
