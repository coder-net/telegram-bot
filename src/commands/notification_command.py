import app
import command_interface as commands


def notification_command(message):
    try:
        date = app.datetime.strptime(message['message']['text'], '%H:%M')
        date = app.datetime.now().replace(hour=date.hour, minute=date.minute, second=0)
        if date < app.datetime.now():
            date += app.dt.timedelta(days=1)
    except ValueError:
        return 'Incorrect format of time. Try "hh:mm"'
    chat_id = message['message']['chat']['id']
    app.schedule.notification.update({'chat_id': chat_id}, {'$set': {'time': date}}, upsert=True)