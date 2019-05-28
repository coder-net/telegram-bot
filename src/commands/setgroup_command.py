import re
import app
import command_interface as commands


def setgroup_command(message):
    if not re.fullmatch(r'/setgroup \d+\s*', message['message']['text']):
        return {'text': 'Incorrect usage of /setgroup. Use "/setgroup group_number"'}
    chat_id = message['message']['chat']['id']
    group_number = re.search(r'\d+', message['message']['text']).group(0)
    if not app.db['schedules']['groups'].count_documents({'name': group_number}):
        return {'text': 'Incorrect group number'}
    app.db['schedules']['users_groups'].update_one(
        {'chat_id': chat_id},
        {'$set': {'group': group_number}},
        upsert=True
    )
    return {'text': 'Group {} set successfully'.format(group_number)}


commands.Command(
    '/setgroup',
    setgroup_command,
    '/setgroup - set your study group'
)
