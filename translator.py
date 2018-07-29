import gspread
from oauth2client.service_account import ServiceAccountCredentials

KEY_FILE = 'Gspread-39d43309c65c.json'


class Translator(object):
    def __init__(self, key_file=KEY_FILE):
        self.key_file = key_file
        self.gc = self.get_google_spreadsheet()
        (self.wp_en_ko, self.wp_en_jp) = self.get_weapon_dict()
        (self.st_en_ko, self.st_en_jp) = self.get_stage_dict()

    def get_google_spreadsheet(self):
        # Authentication
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.key_file, scope)
        # Authorization
        gc = gspread.authorize(credentials)

        return gc

    def get_weapon_dict(self):
        # get worksheet by name
        wks = self.gc.open('Splatoon 2').worksheet('Weapons')
        # create weapon dictionaries
        wp_en_ko = dict()
        wp_en_jp = dict()
        for row in wks.get_all_values()[1:]:
            wp_en_ko[row[1]] = row[2]
            wp_en_jp[row[1]] = row[0]

        return wp_en_ko, wp_en_jp

    def get_stage_dict(self):
        # get worksheet by name
        wks = self.gc.open('Splatoon 2').worksheet('Weapons')
        # create stage dictionaries
        st_en_ko = dict()
        st_en_jp = dict()
        for row in wks.get_all_values()[1:]:
            st_en_ko[row[1]] = row[2]
            st_en_jp[row[1]] = row[0]

        return st_en_ko, st_en_jp