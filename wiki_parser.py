from bs4 import BeautifulSoup as BS
import datetime


class SplatoonWikiParser(object):
    def __init__(self):
        self.html = bytes()

    def feed(self, data, do_clear = True):
        if do_clear:
            self.html = bytes()
        self.html = self.html + data

    def get_schedule(self):
        times = self.parse_salmon2_times()
        weapons = self.parse_salmon2_weapons()
        stage = self.parse_salmon2_stage()

    def parse_salmon2_times(self):
        soup = BS(self.html, 'html.parser')
        # Get start end time
        times = list()
        salmon_text = soup.find(id='salmon2').text
        # parse time
        salmon_start = salmon_text.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
        salmon_start = datetime.datetime.strptime(salmon_start, '%b %d %H:%M %Y')
        salmon_start = salmon_start + datetime.timedelta(hours=9)
        times.append(salmon_start)
        salmon_end = salmon_text.split('-')[1].strip()[:-4] + ' ' + str(datetime.datetime.now().year)
        salmon_end = datetime.datetime.strptime(salmon_end, '%b %d %H:%M %Y')
        salmon_end = salmon_end + datetime.timedelta(hours=9)
        times.append(salmon_end)

        return times

    def parse_salmon2_weapons(self):
        soup = BS(self.html, 'html.parser')
        # parse weapons
        weapons = list()
        weapon = soup.find_all('table',
                               style='width: 100%; border-spacing: 0px; overflow: hidden; table-layout: fixed;')[2]
        weapon = weapon.find_all('table', style='width: 100%; border-spacing: 0px;')[1]
        weapon = weapon.text.split('\n')
        for text in weapon:
            if len(text) > 0:
                weapons.append(text)

        return weapons

    def parse_salmon2_stage(self):
        soup = BS(self.html, 'html.parser')
        # parse stage
        stage = soup.find_all('td',
                               style='background-color: rgba(255, 255, 255, 0.4); border: 2px solid #ffffff; border-width: 0px 0px 2px 2px; border-radius: 0px 0px 0px 8px; text-align: center;')
        stage = stage[1].text

        return stage

