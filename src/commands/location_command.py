import app
import command_interface as commands
from weather_tools import get_weather


def location_command(message):
    if not 'location' in message['message']:
        text = "Command isn't found"
    else:
        app.send_message(
            message['message']['chat']['id'],
            {
                'text': 'Detele buttons',
                'reply_markup': {
                    'remove_keyboard': True
                }
            })
    text = get_weather(
        message['message']['location']['latitude'],
        message['message']['location']['longitude']
    )
    return {'text': text, 'parse_mode': 'Markdown'}


commands.Command(
    '/location',
    location_command,
    '`/location` - get weather for given location'
)