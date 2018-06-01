import datetime

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