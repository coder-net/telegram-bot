import command_interface as commands


def weather_command(message):
    return {
        'text': 'Send your location, please',
        'reply_markup': {
            'keyboard': [[
                {
                    'text': '/location',
                    'request_location': True
                },
                '/cancel'
            ]]
        }
    }


commands.Command(
    '/weather',
    weather_command,
    '`/weather` - get current weather'
)