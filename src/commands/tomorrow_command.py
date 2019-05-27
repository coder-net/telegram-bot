import app
import command_interface as commands
from schedule_tools import get_schedule


def tomorrow_command(message):
    group_number = message['message']['text'].split()[-1]
    day =  app.dt.datetime.today().weekday()
    week = (app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'] + (day == 0)) % 4 + (day == 0)
    schedule = get_schedule(
            day,
            week,
            group_number
        )
    return 'Group: {} | {}, {} week\n\n{}'.format(
            group_number,
            (app.dt.datetime.today() + app.dt.datetime.timedelta(days=1)).strftime('%A, %d.%m'),
            week + 1,
            schedule
    )


commands.Command(
    [r'/tomorrow +\d+\s*'],
    tomorrow_command,
    "/tomorrow group_number - get tomorrow's schedule for group_number"
)
