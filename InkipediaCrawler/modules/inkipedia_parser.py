from bs4 import BeautifulSoup
import datetime

FILENAME = 'latest.html'


class InkipediaParser(object):
    def __init__(self, file_name=FILENAME):
        self.file_name = file_name
        with open(self.file_name, 'r') as f:
            self.soup = BeautifulSoup(f.read(), 'html.parser')

    def get_salmonrun_schedule(self):
        times = self._parse_salmonrun_times()
        weapons = self._parse_salmonrun_weapons()
        stages = self._parse_salmonrun_stages()
        schedules = list()
        for index in range(0, 2):
            schedule = {'start_time': times[index][0],
                        'end_time': times[index][1],
                        'weapon1': weapons[index][0],
                        'weapon2': weapons[index][1],
                        'weapon3': weapons[index][2],
                        'weapon4': weapons[index][3],
                        'stage': stages[index]}
            schedules.append(schedule)

        return schedules

    def _parse_salmonrun_times(self):
        tz_seoul = datetime.timezone(datetime.timedelta(hours=9))
        identifiers = ['salmon1', 'salmon2']
        # Get start end time
        times = list()
        for identifier in identifiers:
            salmon_text = self.soup.find(id=identifier).text
            # parse time
            salmon_start = salmon_text.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
            salmon_start = datetime.datetime.strptime(salmon_start, '%b %d %H:%M %Y')
            salmon_start = salmon_start + datetime.timedelta(hours=9)  # KTC = +9000
            salmon_start = salmon_start.replace(tzinfo=tz_seoul)
            salmon_end = salmon_text.split('-')[1].strip()[:-4] + ' ' + str(datetime.datetime.now().year)
            salmon_end = datetime.datetime.strptime(salmon_end, '%b %d %H:%M %Y')
            salmon_end = salmon_end + datetime.timedelta(hours=9)  # KTC = +9000
            salmon_end = salmon_end.replace(tzinfo=tz_seoul)
            times.append((salmon_start.isoformat(), salmon_end.isoformat()))
        return times

    def _parse_salmonrun_weapons(self):
        soup = self.soup
        identifiers = [0, 1]
        weapons = list()
        # parse weapons
        for identifier in identifiers:
            weapon = soup.find_all('table',
                                   style='width: 100%; border-spacing: 0px;')[identifier]
            weapon = weapon.text.split('\n')
            four_weapon = list()
            for text in weapon:
                if len(text) > 0:
                    four_weapon.append(text.strip())
            weapons.append(four_weapon)

        return weapons

    def _parse_salmonrun_stages(self):
        soup = self.soup
        identifiers = [0, 1]
        stages = list()
        for identifier in identifiers:
            # parse stage
            stage = soup.find_all('td',
                                  style=('background-color: rgba(255, 255, 255, 0.4); '
                                         'border: 2px solid #ffffff; '
                                         'border-width: 0px 0px 2px 2px; '
                                         'border-radius: 0px 0px 0px 8px; '
                                         'text-align: center;'))
            stage = stage[identifier].text.strip()
            stages.append(stage)

        return stages
