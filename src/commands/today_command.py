import app
import command_interface as commands
from schedule_tools import get_schedule


def today_command(message):
    group_number = message['message']['text'].split()[-1]
    day = app.dt.datetime.today().weekday()
    week = app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week']
    schedule = get_schedule(
            day,
            week,
            group_number
        )
    return 'Group: {} | {}, {} week\n\n{}'.format(
        group_number,
        app.dt.datetime.today().strftime('%A, %d.%m'),
        week + 1,
        schedule
    )


commands.Command(
    [r'/today +\d+\s*'],
    today_command,
    "/today group_number - get today's schedule for group_number"
)

