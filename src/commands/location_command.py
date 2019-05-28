import app
import command_interface as commands
from weather_tools import get_weather


def location_command(message):
    if not 'location' in message['message']:
        text = "Command isn't found"
    text = get_weather(
        message['message']['location']['latitude'],
        message['message']['location']['longitude']
    )
    return {'text': text, 'parse_mode': 'Markdown', 'reply_markup': {'remove_keyboard': True}}


commands.Command(
    '/location',
    location_command,
    '/location - get weather for given location'
)
