import app


def get_schedule(curr_day, curr_week, group_number):
    if not app.db.schedules.groups.count_documents({'name': group_number}):
        return 'No such group'
    schedule = app.db.schedules.groups.find_one({'name': group_number})
    res = ''
    for subj in schedule['schedule'][curr_day]['schedule']:
        if curr_week in subj['weekNumber']:
            res += '{} {} -  {} ({}) {}\n'.format(
                subj['lessonTime'],
                subj['auditory'],
                subj['subject'],
                subj['lessonType'],
                '' if not subj['numSubgroup'] else '{{{} subgr.}}'.format(subj['numSubgroup'])
            )

    return res if res else 'No subjects at this day'
