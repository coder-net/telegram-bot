import datetime
import requests
import threading
from timeloop import Timeloop
from pymongo import MongoClient


tl = Timeloop()


s = requests.Session()


client = MongoClient('localhost', 27017)
db = client.bot


schedule_api = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup='
update_api = 'https://journal.bsuir.by/api/v1/studentGroup/lastUpdateDate?studentGroup='
week_api = 'http://journal.bsuir.by/api/v1/week'


@tl.job(interval=datetime.timedelta(seconds=600))
def week_update():
    try:
        week = s.get(week_api).json()
    except:
        pass
    else:
        db.schedules.date.update(
                {'name': 'curr_week'},
                {'$set': {'curr_week': week}}
        )


@tl.job(interval=datetime.timedelta(seconds=60*60*6))
def schedule_update_check():
    for group in db.schedules.groups.find():
        try:
            lastUpdate = s.get(update_api + group['name']).json()['lastUpdateDate']
        except:
            continue
        if lastUpdate != group['lastUpdateDate']:
            schedule_update(group['name'])


def schedule_update(group_number):
    try:
        schedule = s.get(schedule_api + group_number).json()
    except:
        return
    db.schedule.groups.update(
            {'name': group_number},
            {'$set': {'schedule': schedule['schedules']}},
            upsert=True
    )


if __name__ == '__main__':
    tl.start(block=True)
