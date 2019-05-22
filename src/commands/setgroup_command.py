import app
import command_interface as commands


def setgroup_command(message):
    chat_id = message['message']['chat']['id']
    group_number = message['message']['text'].split()[-1]
    if not app.db['schedules']['groups'].count_documents({'name': group_number}):
        return 'Incorrect group number'
    # if not app.db['schedules']['users_groups'].find({'chat_id': chat_id}):
    #     app.db['schedules']['users_groups'].insert_one({
    #         'char_id' : chat_id,
    #         'group' : group_number
    #     })
    # else:
    app.db['schedules']['users_groups'].update_one(
        {'chat_id': chat_id},
        {'$set':{'group': group_number}},
        upsert=True
    )
    return 'Set successfully'


setgroup = commands.Command()
setgroup.description = 'set your study group'
setgroup.keys = [r'/setgroup \d+\s*']
setgroup.handle = setgroup_command
