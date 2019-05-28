import re
import requests
import command_interface as commands


def cfrating_command(message):
    url = 'http://codeforces.com/api/user.rating?handle='
    if not re.fullmatch(r'/cfrating \w+\s*', message['message']['text']):
        return {'text': 'Incorrect usage of /cfrating command. Use /cfrating handle'}
    handle = message['message']['text'].split()[-1]
    try:
        rating = requests.get(url + handle).json()
    except:
        return {'text':'Error. Codeforces API is unavailable now'}
    if rating['status'] != 'OK':
        return {'text': rating['comment']}
    if len(rating['result']) == 0:
        return {'text': "Don't take part in any contests"}
    return {
        'text': '`Contest name:` *{}*\n`Rank:` {}\n`Old rating:` {}\n`New rating:` {}\n`Difference:` {}'.format(
            rating['result'][-1]['contestName'],
            rating['result'][-1]['rank'],
            rating['result'][-1]['oldRating'],
            rating['result'][-1]['newRating'],
            rating['result'][-1]['newRating'] - rating['result'][-1]['oldRating']
        ),
        'parse_mode': 'Markdown'
    }


commands.Command(
    '/cfrating',
    cfrating_command,
    '/cfrating handle - get your results from last constest'
)
