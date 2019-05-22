import app
import command_interface as commands
from schedule_tools import get_schedule


def tomorrow_default_command(message):
    chat_id = message['message']['chat']['id']
    if not app.db.schedules.users_groups.count_documents({'chat_id': chat_id}):
        return 'Set your study group (//setgroup)'
    day =  (app.db.schedules.date.find_one({'name': 'curr_day'})['curr_day'] + 1) % 7
    week = (app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'] + (day == 0)) % 4 + (day == 0)
    return get_schedule(
            day,
            week,
            app.db.schedules.users_groups.find_one({'chat_id': chat_id})['group']
        )


tomorrow_default = commands.Command()
tomorrow_default.description = "get tomorrow's schedule for your group"
tomorrow_default.keys = [r'/tomorrow\s*']
tomorrow_default.handle = tomorrow_default_command

