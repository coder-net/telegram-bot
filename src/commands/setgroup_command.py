import app
import command_interface as commands


def setgroup_command(message):
    chat_id = message['message']['chat']['id']
    group_number = message['message']['text'].split()[-1]
    if not app.db['schedules']['groups'].count_documents({'name': group_number}):
        return 'Incorrect group number'
    app.db['schedules']['users_groups'].update_one(
        {'chat_id': chat_id},
        {'$set':{'group': group_number}},
        upsert=True
    )
    return 'Set successfully'


commands.Command(
    [r'/setgroup \d+\s*'],
    setgroup_command,
    '/setgroup - set your study group'
)
