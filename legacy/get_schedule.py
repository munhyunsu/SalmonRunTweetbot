import urllib.request
from bs4 import BeautifulSoup as BS
import datetime

def get_schedule():
    should_post = [False, False]
    with urllib.request.urlopen('https://splatoonwiki.org/wiki/Main_Page') as f:
        soup = BS(f.read(), 'html.parser')

        # Get start end time
        salmon1 = soup.find(id='salmon1').text
        salmon2 = soup.find(id='salmon2').text
        # parse time
        salmon1_start = salmon1.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
        salmon1_start = datetime.datetime.strptime(salmon1_start, '%b %d %H:%M %Y')
        salmon1_start = salmon1_start + datetime.timedelta(hours = 9)
        salmon1_end = salmon1.split('-')[1].strip()[:-4] + ' ' + str(datetime.datetime.now().year)
        salmon1_end = datetime.datetime.strptime(salmon1_end, '%b %d %H:%M %Y')
        salmon1_end = salmon1_end + datetime.timedelta(hours = 9)
        salmon2_start = salmon2.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
        salmon2_start = datetime.datetime.strptime(salmon2_start, '%b %d %H:%M %Y')
        salmon2_start = salmon2_start + datetime.timedelta(hours = 9)
        salmon2_end = salmon2.split('-')[1].strip()[:-4] + ' ' + str(datetime.datetime.now().year)
        salmon2_end = datetime.datetime.strptime(salmon2_end, '%b %d %H:%M %Y')
        salmon2_end = salmon2_end + datetime.timedelta(hours = 9)
        # print((salmon1_end - salmon1_start).total_seconds())
        # print(salmon1_start.strftime('%m/%d %H:%M'))

        weapont1 = soup.find_all('table', style = 'width: 100%; border-spacing: 0px; overflow: hidden; table-layout: fixed;')[2]
        weapont1 = weapont1.find_all('table', style = 'width: 100%; border-spacing: 0px;')[0]
        weapont1 = weapont1.text.split('\n')
        weapon1 = list()
        for text in weapont1:
            if len(text) > 0:
                weapon1.append(text)
        del(weapont1)
        weapont2 = soup.find_all('table', style = 'width: 100%; border-spacing: 0px; overflow: hidden; table-layout: fixed;')[2]
        weapont2 = weapont2.find_all('table', style = 'width: 100%; border-spacing: 0px;')[1]
        weapont2 = weapont2.text.split('\n')
        weapon2 = list()
        for text in weapont2:
            if len(text) > 0:
                weapon2.append(text)
        del(weapont2)

        stage1 = soup.find_all('td', style = 'background-color: rgba(255, 255, 255, 0.4); border: 2px solid #ffffff; border-width: 0px 0px 2px 2px; border-radius: 0px 0px 0px 8px; text-align: center;')
        stage1 = stage1[0].text
        stage2 = soup.find_all('td', style='background-color: rgba(255, 255, 255, 0.4); border: 2px solid #ffffff; border-width: 0px 0px 2px 2px; border-radius: 0px 0px 0px 8px; text-align: center;')
        stage2 = stage2[1].text

    return (salmon1_start, salmon1_end, weapon1, stage1, salmon2_start, salmon2_end, weapon2, stage2)

# get_schedule()