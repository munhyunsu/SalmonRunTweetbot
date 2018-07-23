import time
import datetime
import urllib.request

def should_post(salmon_times, now = datetime.datetime.now()):
    (start, plan, end) = (False, False, False)
    start_sec = (salmon_times[0] - now).total_seconds()
    if (start_sec <= (3600-1800)) and (start_sec > (0-1800)):
        start = True
    if (start_sec <= (21600+1800)) and (start_sec > (18000+1800)):
        plan = True
    end_sec = (salmon_times[1] - now).total_seconds()
    if (end_sec <= (0+1800)) and (end_sec > (-3600+1800)):
        end = True

    return (start, plan, end)


def should_post2(schedule, now = datetime.datetime.now()):
    (start, plan, end) = (False, False, False)
    start_sec = (schedule['start_time'] - now).total_seconds()
    if (start_sec <= (3600-1800)) and (start_sec > (0-1800)):
        start = True
    if (start_sec <= (21600+1800)) and (start_sec > (18000+1800)):
        plan = True
    end_sec = (schedule['end_time'] - now).total_seconds()
    if (end_sec <= (0+1800)) and (end_sec > (-3600+1800)):
        end = True

    return (start, plan, end)


def should_post3(schedule_list, now = datetime.datetime.now()):
    result = dict()
    for schedule in schedule_list:
        start_sec = (schedule['start_time'] - now).total_seconds()
        if (start_sec <= (3600 - 1800)) and (start_sec > (0 - 1800)):
            result['start'] = schedule
        if (start_sec <= (21600 + 1800)) and (start_sec > (18000 + 1800)):
            result['plan'] = schedule
        end_sec = (schedule['end_time'] - now).total_seconds()
        if (end_sec <= (0 + 1800)) and (end_sec > (-3600 + 1800)):
            result['end'] = schedule

    return result


# def check_internet(max_try = 30, sleep_sec = 60, url = 'https://www.google.com/'):
#     '''
#     dedicated!
#     :param max_try:
#     :param sleep_sec:
#     :param url:
#     :return:
#     '''
#     for index in range(0, max_try):
#         try:
#             urllib.request.urlopen(url, timeout = 10)
#             return True
#         except:
#             if index == (max_try-1):
#                 return False
#             print('{0}: Can not reach internet(loop: {1})'.format(datetime.datetime.now(), index+1))
#             time.sleep(sleep_sec)
#             continue
