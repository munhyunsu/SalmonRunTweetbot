import datetime


class Coordinator(object):
    def __init__(self):
        self.schedule_list = None

    def feed_schedule_list(self, schedule_list):
        self.schedule_list = schedule_list

    def get_start_schedule(self, now=datetime.datetime.now()):
        for schedule in self.schedule_list:
            start_sec = (schedule['start_time'] - now).total_seconds()
            if (start_sec < 1800) and (start_sec > -1800):
                return schedule
        return None

    def get_end_schedule(self, now=datetime.datetime.now()):
        schedule_list = self.schedule_list
        for index in range(0, len(schedule_list)):
            end_sec = (schedule_list[index]['end_time'] - now).total_seconds()
            if (end_sec < 1800) and (end_sec > -1800):
                if len(schedule_list) > index+1:
                    return schedule_list[index+1]
        return None

    def get_plan_schedule(self, now=datetime.datetime.now()):
        for schedule in self.schedule_list:
            start_sec = (schedule['start_time'] - now).total_seconds()
            if (start_sec < 23400) and (start_sec > 19800):
                return schedule
        return None
