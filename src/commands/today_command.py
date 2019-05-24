import app
import command_interface as commands
from schedule_tools import get_schedule


def today_command(message):
    group_number = message['message']['text'].split()[-1]
    return get_schedule(
            app.db.schedules.date.find_one({'name': 'curr_day'})['curr_day'],
            app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'],
            group_number
        )


commands.Command(
    today_command,
    today_command,
    [r'/today +\d+\s*'],
    "/today group_number - get today's schedule for group_number"
)

