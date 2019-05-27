import re
import app
import command_interface as commands
from schedule_tools import get_schedule


def schedule_command(message):
    command = re.match(r'^/\w+', message['message']['text']).group(0)
    # get group
    if not re.fullmatch(r'{}(\s*)|(\d+\s*)'.format(command), message['message']['text']):
        return {
            'text': 'Incorrect usage of `{0}` command. Use `{0} [group_number]`'.format(command),
            'parse_mode': 'Markdown'
        }
    try:
        group_number = re.search(r'\d+', message['message']['text']).group(0)
    except AttributeError:
        if not app.db.schedules.users_groups.count_documents({'chat_id': message['message']['chat']['id']}):
            return {
                'text': 'Set your study group (`/setgroup`)',
                'parse_mode': 'Markdown'
                }
        group_number = app.db.schedules.users_groups.find_one({'chat_id': message['message']['chat']['id']})['group']
    # values to get schedule
    if command == '/today':
        day = app.dt.datetime.today().weekday()
        week = app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week']
    else:
        day = app.dt.datetime.today() + app.dt.datetime.timedelta(days=1)
        week = (app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'] + (day == 0)) % 4 + (day == 0)
    schedule = get_schedule(
            day.weekday(),
            week,
            group_number
        )
    return {
        'text': 'Group: *{}* | {}, {} week\n\n{}'.format(
            group_number,
            day.strftime('%A, %d.%m'),
            week + 1,
            schedule
        ),
        'parse_mode': 'Markdown'
    }


commands.Command(
    '/today',
    schedule_command,
    "`/today [group_number]` - get today's schedule"
)
commands.Command(
    '/tomorrow',
    schedule_command,
    "/tomorrow [group_number]` - get tomorrow's schedule"
)
