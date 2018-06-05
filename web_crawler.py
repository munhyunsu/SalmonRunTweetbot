import urllib.request
from bs4 import BeautifulSoup as BS
import datetime

class WebCrawler(object):
    def __init__(self, baseurl = 'https://splatoonwiki.org'):
        self.baseurl = baseurl
        self.mainpage = None

    def get_mainpage(self):
        '''
        :return: HTML of main page
        '''
        url = self.baseurl + '/wiki/Main_Page'
        if self.mainpage == None:
            with urllib.request.urlopen(url) as f:
                self.mainpage = f.read()
        return self.mainpage

    def get_schedule(self):
        '''
        :return: list of salmonrun times
                 [(salmon1_start, salmon1_end), (salmon2_start, salmon2_end)]
        '''
        mainpage = self.get_mainpage()
        soup = BS(mainpage, 'html.parser')

        # results
        salmon_times = list()
        ids = ['salmon1', 'salmon2']

        # loop salmon run 1 and 2
        for index in range(0, len(ids)):
            # Get start end time
            salmon_text = soup.find(id=ids[index]).text
            # parse time
            salmon_start = salmon_text.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
            salmon_start = datetime.datetime.strptime(salmon_start, '%b %d %H:%M %Y')
            salmon_start = salmon_start + datetime.timedelta(hours=9)
            salmon_end = salmon_text.split('-')[1].strip()[:-4] + ' ' + str(datetime.datetime.now().year)
            salmon_end = datetime.datetime.strptime(salmon_end, '%b %d %H:%M %Y')
            salmon_end = salmon_end + datetime.timedelta(hours=9)
            salmon_times.append((salmon_start, salmon_end))

        return salmon_times

    def get_weapon(self):
        '''
        :return: list of salmonrun weapons
                 [[salmon1_weapons], [salmon2_weapons]]
        '''
        mainpage = self.get_mainpage()
        soup = BS(mainpage, 'html.parser')

        # results
        salmon_weapons = list()

        # loop salmon run weapons of 1 and 2
        for index in range(0, 2):
            weapons = list()
            weapon = soup.find_all('table',
                                   style='width: 100%; border-spacing: 0px; overflow: hidden; table-layout: fixed;')[2]
            weapon = weapon.find_all('table', style='width: 100%; border-spacing: 0px;')[index]
            weapon = weapon.text.split('\n')
            for text in weapon:
                if len(text) > 0:
                    weapons.append(text)
            salmon_weapons.append(weapons)

        return salmon_weapons

    def get_stage(self):
        '''
        :return: list of salmonrun stage
                 [salmon1_stage, salmon2_stage]
        '''
        mainpage = self.get_mainpage()
        soup = BS(mainpage, 'html.parser')

        # results
        salmon_stages = list()

        # loop salmon run weapons of 1 and 2
        for index in range(0, 2):
            stage = soup.find_all('td',
                                   style='background-color: rgba(255, 255, 255, 0.4); border: 2px solid #ffffff; border-width: 0px 0px 2px 2px; border-radius: 0px 0px 0px 8px; text-align: center;')
            stage = stage[index].text
            salmon_stages.append(stage)

        return salmon_stages

    def get_img_weapon(self):
        '''
        :return: list of salmonrun weapons
                 [[salmon1_img_weapons], [salmon2_img_weapons]]
        '''
        mainpage = self.get_mainpage()
        soup = BS(mainpage, 'html.parser')

        weapon = soup.find_all('table',
                               style='width: 100%; border-spacing: 0px; overflow: hidden; table-layout: fixed;')[2]
        weapon = weapon.find_all('table', style='width: 100%; border-spacing: 0px;')[0]
        weapon_subpages = weapon.find_all('a')

        for tags in weapon_subpages:
            if len(tags.text) == 0:
                continue
            url = self.baseurl + tags['href']

            print(url)
