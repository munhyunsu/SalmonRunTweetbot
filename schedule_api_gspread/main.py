import os
import time
import datetime
import random
import urllib.request
import urllib.parse
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

    gc = gspread.service_account(filename=FLAGS.service_account)
    
    sh = gc.open_by_key(config.sheet_key)
    wsh = sh.worksheet('Queue')
    
    list_of_dicts = wsh.get_all_records()

    for item in list_of_dicts:
        value = {'timestart': get_unixtime(item['Start Time']),
                 'timeend': get_unixtime(item['End Time']),
                 'stage': item['Stage'],
                 'weapon1': item['Weapon 1'],
                 'weapon2': item['Weapon 2'],
                 'weapon3': item['Weapon 3'],
                 'weapon4': item['Weapon 4'],
                }
        #data = urllib.parse.urlencode(json.dumps(value)).encode('utf-8')
        data = json.dumps(value).encode('utf-8')
        params = urllib.parse.urlencode({'api_key': config.api_key})
        headers = {'accept': 'application/json',
                   'Content-Type': 'application/json'}
        url = f'{config.endpoint}/salmonrun/?{params}'
        req = urllib.request.Request(url=url,
                                     data=data,
                                     headers=headers,
                                     method='POST')
        if DEBUG:
            print(f'[{time.time()-STIME}] Request {url} with {data}')
        with urllib.request.urlopen(req) as f:
            print(f.read().decode('utf-8'))
        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    import argparse

    root_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(root_path)
    os.chdir(root_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')
    parser.add_argument('--service_account', default='./service_account.json',
                        help='The service account json file')

    FLAGS, _ = parser.parse_known_args()
    DEBUG = FLAGS.debug

    main()

