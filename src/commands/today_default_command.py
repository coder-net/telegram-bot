import app
import command_interface as commands
from schedule_tools import get_schedule


def today_default_command(message):
    chat_id = message['message']['chat']['id']
    if not app.db.schedules.users_groups.count_documents({'chat_id': chat_id}):
        return 'Set your study group (//setgroup)'
    return get_schedule(
            app.db.schedules.date.find_one({'name': 'curr_day'})['curr_day'],
            app.db.schedules.date.find_one({'name': 'curr_week'})['curr_week'],
            app.db.schedules.users_groups.find_one({'chat_id': chat_id})['group']
        )


today_default = commands.Command()
today_default.description = "get today's schedule for your group"
today_default.keys = [r'/today\s*']
today_default.handle = today_default_command
