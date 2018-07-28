import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_translate_dict():
    # Authentication
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Gspread-39d43309c65c.json', scope)
    # Authorization
    gc = gspread.authorize(credentials)

    # get worksheet by name
    wks = gc.open('Splatoon 2').worksheet('Weapons')
    # create weapon dictionaries
    wp_en_ko = dict()
    wp_en_jp = dict()
    for row in wks.get_all_values()[1:]:
        wp_en_ko[row[1]] = row[2]
        wp_en_jp[row[1]] = row[0]


    wks = gc.open('Splatoon 2').worksheet('Stages')
    # create stage dictionaries
    st_en_ko = dict()
    st_en_jp = dict()
    for row in wks.get_all_values()[1:]:
        st_en_ko[row[1]] = row[2]
        st_en_jp[row[1]] = row[0]

    return (wp_en_jp, wp_en_ko, st_en_jp, st_en_ko)

# print(get_translate_dict())