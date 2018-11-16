import os
import copy
import datetime

from PIL import Image, ImageFont, ImageDraw
from twitter_bot.modules.file_handler import FileHandler
from twitter_bot.modules.coordinator import ISO8601


def get_files(path, ext='', recursive=False):
    import os
    path_list = [path]

    while len(path_list) > 0:
        cpath = path_list.pop()
        with os.scandir(cpath) as it:
            for entry in it:
                # if not entry.name.startswith('.') and entry.is_file():
                if entry.is_file():
                    if entry.name.endswith(ext):
                        yield entry.path
                else:
                    if recursive:
                        path_list.append(entry.path)

    return path_list


class ImageHandler(object):
    def __init__(self, ipath):
        self.ipath = ipath
        self.images = dict()
        self.file_handler = FileHandler()

    def get_original_images(self):
        images = self.images
        if len(images) != 0:
            return images
        for path in get_files(self.ipath):
            name = os.path.basename(path)
            name = name[:-4]  # remove ext
            images[name] = path

        return images

    def get_merged_image(self, schedule):
        target = copy.deepcopy(schedule)
        if os.path.exists(self.file_handler.file_name):
            url = self.file_handler.read()
            target['tweet_url'] = url
        start_time = ''.join(schedule['start_time'].rsplit(':', 1))
        start_time = datetime.datetime.strptime(start_time, ISO8601)
        target['start_time'] = start_time
        end_time = ''.join(schedule['end_time'].rsplit(':', 1))
        end_time = datetime.datetime.strptime(end_time, ISO8601)
        target['end_time'] = end_time
        # prepare materials
        images = self.get_original_images()
        image_title = '{stage}/{stage_jp}'.format_map(target)
        image_date = '{start_time:%m/%d %H:%M} - {end_time:%m/%d %H:%M}'.format_map(target)
        stage_name = target['stage']
        weapon_names = [target['weapon1'],
                        target['weapon2'],
                        target['weapon3'],
                        target['weapon4']]
        stage = Image.open(images[stage_name])
        weapons = list()
        for weapon_name in weapon_names:
            weapon = Image.open(images[weapon_name])
            weapons.append(weapon)
        mask = Image.open(images['mask'])

        merged_image = Image.new("RGBA", (1920, 1080))
        merged_image.paste(stage.resize((1920, 1080)), (0, 0))
        merged_image.alpha_composite(mask)
        for index in range(0, len(weapons)):
            resized_weapon = weapons[index].resize((480, 480))
            merged_image.paste(resized_weapon, (480*index, 1080-480), resized_weapon)

        font_title = ImageFont.truetype('fonts/Splat2K.ttf', 80)
        font_date = ImageFont.truetype('fonts/Splat2K.ttf', 60)

        draw = ImageDraw.Draw(merged_image, "RGBA")
        draw.text((50, 15), image_title, (0, 0, 0), font=font_title)
        draw.text((50, 95), image_date, (220, 118, 40), font=font_date)

        save_path = 'merged_image.png'
        with open(save_path, 'wb') as f:
            merged_image.save(f, 'png')

        return save_path
