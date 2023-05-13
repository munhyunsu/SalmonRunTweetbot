import os
import time
import datetime
import urllib.request
import urllib.parse
import json
import pprint

import tweepy

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

    timecurrent = int(time.time())
    timescurrent = get_time(timecurrent, tz=TZ_SEOUL)
    if DEBUG:
        print(f'[{time.time()-STIME}] {timecurrent=}')
        print(f'[{time.time()-STIME}] {timescurrent=}')

    url = f'{config.endpoint}/salmonrun/'
    headers = {'accept': 'application/json'}
    req = urllib.request.Request(url=url,
                                 headers=headers)

    data = []
    with urllib.request.urlopen(req) as f:
        response = f.read().decode('utf-8')
        data = json.loads(response)
        if DEBUG:
            print(f'[{time.time()-STIME}] RESTful API: {data=}')

    # Dangeronous coding
    schedule1 = data[0]
    schedule2 = data[1]
    if DEBUG:
        print(f'[{time.time()-STIME}] {schedule1=}')
        print(f'[{time.time()-STIME}] {schedule2=}')

    schedule1_timediff = timecurrent - schedule1['timestart']
    if DEBUG:
        print(f'[{time.time()-STIME}] {schedule1_timediff=}')
        print(f'[{time.time()-STIME}] {config.time_maxdiff=}')
        print(f'[{time.time()-STIME}] {config.status_hours=}')
        print(f'[{time.time()-STIME}] {(abs(schedule1_timediff) < config.time_maxdiff)=}')
        print(f'[{time.time()-STIME}] {(timescurrent.hour in config.status_hours)=}')


    text = ''
    if abs(schedule1_timediff) < config.time_maxdiff:
        text = f'''<새먼 런 시작>

[지금 ~ {get_time(schedule1['timeend'], tz=TZ_SEOUL).strftime('%m/%d %H:%M')}]
스테이지 - {schedule1['stage']}
무기 - {schedule1['weapon1']}/{schedule1['weapon2']}/{schedule1['weapon3']}/{schedule1['weapon4']}

[다음 ~ {get_time(schedule2['timeend'], tz=TZ_SEOUL).strftime('%m/%d %H:%M')}]
스테이지 - {schedule2['stage']}
무기 - {schedule2['weapon1']}/{schedule2['weapon2']}/{schedule2['weapon3']}/{schedule2['weapon4']}'''
    elif timescurrent.hour in config.status_hours:
        text = f'''<새먼 런 모집중>

[지금 ~ {get_time(schedule1['timeend'], tz=TZ_SEOUL).strftime('%m/%d %H:%M')}]
스테이지 - {schedule1['stage']}
무기 - {schedule1['weapon1']}/{schedule1['weapon2']}/{schedule1['weapon3']}/{schedule1['weapon4']}

[다음 ~ {get_time(schedule2['timeend'], tz=TZ_SEOUL).strftime('%m/%d %H:%M')}]
스테이지 - {schedule2['stage']}
무기 - {schedule2['weapon1']}/{schedule2['weapon2']}/{schedule2['weapon3']}/{schedule2['weapon4']}'''
    if DEBUG:
        print(f'[{time.time()-STIME}] Tweet {text=}')
    
    if FLAGS.text is not None:
        text = FLAGS.text

    if len(text) > 0:
        if DEBUG:
            print(f'[{time.time()-STIME}] Ready to upload')
        client = tweepy.Client(consumer_key=config.consumer_key,
                               consumer_secret=config.consumer_secret,
                               access_token=config.access_token,
                               access_token_secret=config.access_token_secret)
        try:
            tres = client.create_tweet(text=text)
        except tweepy.errors.Unauthorized as e:
            tres = f'{e}'
        if DEBUG:
            print(f'[{time.time()-STIME}] Return {tres=}')
    if DEBUG:
        print(f'[{time.time()-STIME}] End main.py')
        


if __name__ == '__main__':
    import argparse

    root_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(root_path)
    os.chdir(root_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')
    parser.add_argument('--text', type=str,
                        help='(Forced) upload text')

    FLAGS, _ = parser.parse_known_args()
    DEBUG = FLAGS.debug

    main()

