import app
import command_interface as commands
from schedule_tools import get_schedule


def tomorrow_default_command(message):
    chat_id = message['message']['chat']['id']
    if not app.db.schedules.users_groups.count_documents({'chat_id': chat_id}):
        return 'Set your study group (/setgroup)'
    day =  app.dt.datetime.today().weekday()
    week = (app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'] + (day == 0)) % 4 + (day == 0)
    group_number = app.db.schedules.users_groups.find_one({'chat_id': chat_id})['group']
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
    [r'/tomorrow\s*'],
    tomorrow_default_command,
    "/tomorrow - get tomorrow's schedule for your group"
)

