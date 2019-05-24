import app
import command_interface as commands
from schedule_tools import get_schedule


def tomorrow_command(message):
    group_number = message['message']['text'].split()[-1]
    day =  (app.db.schedules.date.find_one({'name': 'curr_day'})['curr_day'] + 1) % 7
    week = (app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'] + (day == 0)) % 4 + (day == 0)
    return get_schedule(
            day,
            week,
            group_number
        )


commands.Command(
    tomorrow_command,
    [r'/tomorrow +\d+\s*'],
    "/tomorrow group_number - get tomorrow's schedule for group_number"
)
