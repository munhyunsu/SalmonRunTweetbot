import os
import time
import hashlib
import secrets
import getpass

FLAGS = _ = None
DEBUG = False
STIME = time.time()


def main():
    if DEBUG:
        print(f'[{time.time()-STIME}] Parsed arguements {FLAGS}')
        print(f'[{time.time()-STIME}] Unparsed arguements {_}')

    m = hashlib.sha256()
    username = input('Username: ').strip()
    m.update(username.encode('utf-8'))
    salt_bytes = secrets.token_bytes(16)
    salt = salt_bytes.hex()
    m.update(salt_bytes)
    m.update(getpass.getpass().strip().encode('utf-8'))
    hpassword = m.hexdigest()

    print(f'API Key: {hpassword}')
    print(f'Write to config.py')


if __name__ == '__main__':
    import argparse

    root_path = os.path.abspath(__file__)
    root_dir = os.path.dirname(root_path)
    os.chdir(root_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true',
                        help='The present debug message')

    FLAGS, _ = parser.parse_known_args()

    main()

