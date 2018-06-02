import time
import datetime
import urllib.request

def should_post(salmon_times, now = datetime.datetime.now()):
    start = False
    plan = False
    end = False
    start_sec = (salmon_times[0] - now).total_seconds()
    if (start_sec <= (3600-1800)) and (start_sec > (0-1800)):
        start = True
    if (start_sec <= (21600+1800)) and (start_sec > (18000+1800)):
        plan = True
    end_sec = (salmon_times[1] - now).total_seconds()
    if (end_sec <= (0+1800)) and (end_sec > (-3600+1800)):
        end = True

    return (start, plan, end)

def check_internet(max_try = 30, sleep_sec = 1, url = 'https://www.google.com/'):
    for index in range(0, max_try):
        try:
            urllib.request.urlopen(url, timeout = 10)
            return True
        except:
            if index == (max_try-1):
                return False
            print('{0}: Can not reach internet(loop: {1})'.format(datetime.datetime.now(), index+1))
            time.sleep(sleep_sec)
            continue