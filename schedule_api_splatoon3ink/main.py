import os
import time
import datetime

FLAGS = _ = None
DEBUG = False
STIME = time.time()

TZ_SEOUL = datetime.timezone(datetime.timedelta(hours=9))
TZ_UTC = datetime.timezone(datetime.timedelta())


def main():
    if DEBUG:
        print(f'[{time.time()-STIME}] Parsed arguements {FLAGS}')
        print(f'[{time.time()-STIME}] Unparsed arguements {_}')


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

