import requests
import command_interface as commands


def cfrating_command(message):
    url = 'http://codeforces.com/api/user.rating?handle='
    handle = message['message']['text'].split()[-1]
    try:
        rating = requests.post(url + handle).json()
    except:
        return 'Error. Codeforces API is unavailable now'
    if rating['status'] != 'OK':
        return rating['comment']
    if len(rating['result']) == 0:
        return "Don't take part in any contests"
    return 'Contest name: {}\nRank: {}\nOld rating: {}\nNew rating: {}\nDifference: {}'.format(
        rating['result']['contestName'],
        rating['result']['rank'],
        rating['result']['oldRating'],
        rating['result']['newRating'],
        rating['result']['newRating'] - rating['result']['oldRating']
    )


commands.Command(
    [r'/cfrating \w+'],
    cfrating_command,
    '/cfrating handle - gett your results from last constest'
)