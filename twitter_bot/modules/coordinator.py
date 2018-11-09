import datetime

ISO8601 = '%Y-%m-%dT%H:%M:%S%z'
TIMEZONE = datetime.timezone(datetime.timedelta(hours=9))


class Coordinator(object):
    def __init__(self, schedules):
        self.schedules = schedules

    def get_start_schedule(self, now=datetime.datetime.now(TIMEZONE)):
        for schedule in self.schedules:
            start_time = ''.join(schedule['start_time'].rsplit(':', 1))
            start_time = datetime.datetime.strptime(start_time, ISO8601)
            end_time = ''.join(schedule['end_time'].rsplit(':', 1))
            end_time = datetime.datetime.strptime(end_time, ISO8601)
            start_sec = (start_time - now).total_seconds()
            if (start_sec < 1800) and (start_sec > -1800):
                return schedule
        return None

    def get_1h_before_end_schedule(self, now=datetime.datetime.now(TIMEZONE)):
        for schedule in self.schedules:
            start_time = ''.join(schedule['start_time'].rsplit(':', 1))
            start_time = datetime.datetime.strptime(start_time, ISO8601)
            end_time = ''.join(schedule['end_time'].rsplit(':', 1))
            end_time = datetime.datetime.strptime(end_time, ISO8601)
            end_sec = (end_time - now).total_seconds()
            if (end_sec < 5400) and (end_sec > 1800):
                return schedule
        return None

    def get_end_schedule(self, now=datetime.datetime.now(TIMEZONE)):
        if ((not self._is_open(now=now)) and
                (self._is_open(now=now - datetime.timedelta(hours=1)))):
            for schedule in self.schedules:
                start_time = ''.join(schedule['start_time'].rsplit(':', 1))
                start_time = datetime.datetime.strptime(start_time, ISO8601)
                end_time = ''.join(schedule['end_time'].rsplit(':', 1))
                end_time = datetime.datetime.strptime(end_time, ISO8601)
                start_sec = (start_time - now).total_seconds()
                if start_sec > 0:
                    return schedule
        return None

    def _is_open(self, now=datetime.datetime.now(TIMEZONE)):
        for schedule in self.schedules:
            start_time = ''.join(schedule['start_time'].rsplit(':', 1))
            start_time = datetime.datetime.strptime(start_time, ISO8601)
            end_time = ''.join(schedule['end_time'].rsplit(':', 1))
            end_time = datetime.datetime.strptime(end_time, ISO8601)
            start_sec = (start_time - now).total_seconds()
            end_sec = (end_time - now).total_seconds()
            if (start_sec < 0) and (end_sec > 0):
                return True
        return False

    def get_plan_schedule(self, now=datetime.datetime.now(TIMEZONE)):
        for schedule in self.schedules:
            start_time = ''.join(schedule['start_time'].rsplit(':', 1))
            start_time = datetime.datetime.strptime(start_time, ISO8601)
            end_time = ''.join(schedule['end_time'].rsplit(':', 1))
            end_time = datetime.datetime.strptime(end_time, ISO8601)
            start_sec = (start_time - now).total_seconds()
            if (start_sec < 23400) and (start_sec > 19800):
                return schedule
        return None
