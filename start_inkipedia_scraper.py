import os
import json

from InkipediaCrawler.inkipedia_scraper.inkipedia_scraper import save_inkipedia_json
from gspread_handler.modules.gspread_handler import GSpreadHandler

BASEFILE = 'latest_inkipedia.json'
LOCALEFILE = 'latest_inkipedia_locale.json'


def main():
    # prepare data
    save_inkipedia_json()
    gspread = GSpreadHandler('private/Gspread-39d43309c65c.json')
    (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko) = gspread.get_translate_dict()
    with open(BASEFILE, 'r') as f:
        inkipedia_json = json.load(f)

    # translate
    for index in range(0, 2):
        cursor = inkipedia_json['Salmon Run'][index]
        cursor['weapon1_jp'] = wp_en_jp[cursor['weapon1']]
        cursor['weapon1_ko'] = wp_en_ko[cursor['weapon1']]
        cursor['weapon2_jp'] = wp_en_jp[cursor['weapon2']]
        cursor['weapon2_ko'] = wp_en_ko[cursor['weapon2']]
        cursor['weapon3_jp'] = wp_en_jp[cursor['weapon3']]
        cursor['weapon3_ko'] = wp_en_ko[cursor['weapon3']]
        cursor['weapon4_jp'] = wp_en_jp[cursor['weapon4']]
        cursor['weapon4_ko'] = wp_en_ko[cursor['weapon4']]
        # cursor = inkipedia_json['Regular Battle'][index]
        # cursor['stage1_jp'] = st_en_jp[cursor['stage1']]
        # cursor['stage1_ko'] = st_en_ko[cursor['stage1']]
        # cursor['stage2_jp'] = st_en_jp[cursor['stage2']]
        # cursor['stage2_ko'] = st_en_ko[cursor['stage2']]
        # cursor = inkipedia_json['Ranked Battle'][index]
        # cursor['stage1_jp'] = st_en_jp[cursor['stage1']]
        # cursor['stage1_ko'] = st_en_ko[cursor['stage1']]
        # cursor['stage2_jp'] = st_en_jp[cursor['stage2']]
        # cursor['stage2_ko'] = st_en_ko[cursor['stage2']]
        # cursor = inkipedia_json['League Battle'][index]
        # cursor['stage1_jp'] = st_en_jp[cursor['stage1']]
        # cursor['stage1_ko'] = st_en_ko[cursor['stage1']]
        # cursor['stage2_jp'] = st_en_jp[cursor['stage2']]
        # cursor['stage2_ko'] = st_en_ko[cursor['stage2']]

    with open(LOCALEFILE, 'w') as f:
        json.dump(inkipedia_json, f, indent=2, ensure_ascii=False)

    if os.path.exists(BASEFILE):
        os.remove(BASEFILE)


if __name__ == '__main__':
    main()
