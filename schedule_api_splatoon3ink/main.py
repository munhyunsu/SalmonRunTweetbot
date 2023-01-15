import os
import sys
import time
import datetime
import urllib.request
import json

import gspread

import config

FLAGS = _ = None
DEBUG = False
STIME = time.time()

TZ_SEOUL = datetime.timezone(datetime.timedelta(hours=9))
TZ_UTC = datetime.timezone(datetime.timedelta())


def get_time(timestamp, tz=TZ_UTC):
    return datetime.datetime.fromtimestamp(timestamp, tz=tz)


def get_unixtime(timestr):
    return int(datetime.datetime.fromisoformat(timestr).timestamp())


def main():
    if DEBUG:
        print(f'[{time.time()-STIME}] Parsed arguements {FLAGS}')
        print(f'[{time.time()-STIME}] Unparsed arguements {_}')
    '''
    gc = gspread.service_account(filename=FLAGS.service_account)
    
    sh = gc.open_by_key(config.sheet_key)
    wsh = sh.worksheet('Queue')

    # Get written events
    list_of_dicts = wsh.get_all_records()
    queue = {}

    for item in list_of_dicts:
        value = {'timestart': get_unixtime(item['Start Time']),
                 'timeend': get_unixtime(item['End Time']),
                 'stage': item['Stage'],
                 'weapon1': item['Weapon 1'],
                 'weapon2': item['Weapon 2'],
                 'weapon3': item['Weapon 3'],
                 'weapon4': item['Weapon 4'],
                }
        queue[value['timestart']] = value
    '''
    urllib_version = (f'Python-urllib/'
                      f'{sys.version_info.major}.'
                      f'{sys.version_info.minor}.'
                      f'{sys.version_info.micro}')
    headers = {'Accept': 'application/json',
               'User-Agent': f'{config.user_agent};{urllib_version}'}

    # GET locale data from splatoon3.ink
    if not os.path.exists('ko-KR.json'):
        url = f'{config.source_url}/locale/ko-KR.json'
        req = urllib.request.Request(url=url,
                                     headers=headers,
                                     method='GET')
        if DEBUG:
            print(f'[{time.time()-STIME}] Request {url}')
        with urllib.request.urlopen(req) as f:
            locale = json.loads(f.read().decode('utf-8'))
        with open('ko-KR.json', 'w') as f:
            json.dump(locale, f, ensure_ascii=False, indent=True)
    with open('ko-KR.json' ,'r') as f:
        locale = json.load(f)
    if DEBUG:
        print(f'[{time.time()-STIME}] Read ko-KR.json')
        print(f'{locale}')
        print(f'----- -----')
        

    # GET schedule data from splatoon3.ink
    if not os.path.exists('schedules.json'):
        url = f'{config.source_url}/schedules.json'
        req = urllib.request.Request(url=url,
                                     headers=headers,
                                     method='GET')
        if DEBUG:
            print(f'[{time.time()-STIME}] Request {url}')
        with urllib.request.urlopen(req) as f:
            schedules = json.loads(f.read().decode('utf-8'))
        with open('schedules.json', 'w') as f:
            json.dump(schedules, f, ensure_ascii=False, indent=True)
    with open('schedules.json', 'r') as f:
        schedules = json.load(f)
    if DEBUG:
        print(f'[{time.time()-STIME}] Read schedules.json')
        print(f'{schedules}')
        print(f'----- -----')
    
    new_queue = []
    coop_schedules = schedules['data']['coopGroupingSchedule']
    coop_types = ['regularSchedules', 'bigRunSchedules']
    for coop_type in coop_types:
        for node in coop_schedules[coop_type]['nodes']:
            start_time = node['startTime'].replace('Z', '+00:00')
            print(coop_type, node, 
                  get_unixtime(start_time),
                  get_time(get_unixtime(start_time), tz=TZ_SEOUL))
        
        

        
    
    


if __name__ == '__main__':
    import argparse

    root_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(root_path)
    os.chdir(root_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')
    parser.add_argument('--service_account', default='./service_account.json',
                        help='The service account json file that was downloaded from Google API')

    FLAGS, _ = parser.parse_known_args()
    DEBUG = FLAGS.debug

    main()

