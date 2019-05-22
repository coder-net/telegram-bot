import datetime
import requests
import threading
from timeloop import Timeloop
from pymongo import MongoClient


tl = Timeloop()


client = MongoClient('localhost', 27017)
db = client.bot


schedule_api = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup='
update_api = 'https://journal.bsuir.by/api/v1/studentGroup/lastUpdateDate?studentGroup='
week_api = 'http://journal.bsuir.by/api/v1/week'


@tl.job(interval=datetime.timedelta(seconds=60*60))
def date_update():
    db.schedules.date.update(
            {'name': 'curr_day'},
            {'$set': {'curr_day': datetime.datetime.today().weekday()}}
    )
    db.schedules.date.update(
            {'name': 'curr_week'},
            {'$set': {'curr_day': requests.get(week_api).json()}}
    )


@tl.job(interval=datetime.timedelta(seconds=60*60*6))
def schedule_update_check():
    for group in db.schedules.groups.find():
        try:
            lastUpdate = requests.get(update_api + group['name']).json()['lastUpdateDate']
        except:
            continue
        if lastUpdate != group['lastUpdateDate']:
            schedule_update(group['name'])


def schedule_update(group_number):
    try:
        schedule = requests.get(schedule_api + group_number).json()
    except:
        return
    db.schedule.groups.update(
            {'name': group_number},
            {'$set': {'schedule': schedule['schedules']}},
            upsert=True
    )


if __name__ == '__main__':
    tl.start(block=True)
