import os

from PIL import Image

from utils import get_files


class ImageHandler(object):
    def __init__(self, ipath):
        self.ipath = ipath
        self.images = dict()

    def get_original_images(self):
        images = self.images
        if len(images) != 0:
            return images
        for path in get_files(self.ipath):
            name = os.path.basename(path)
            name = name[:-4] # remove ext
            images[name] = path

        return images

    def get_merged_image(self, schedule):
        # prepare materials
        images = self.get_original_images()
        stage_name = schedule['stage_en']
        weapon_names = [schedule['weapon1_en'],
                        schedule['weapon2_en'],
                        schedule['weapon3_en'],
                        schedule['weapon4_en']]
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

        save_path = 'merged_image.png'
        with open(save_path, 'wb') as f:
            merged_image.save(f, 'png')

        return save_path

# new = Image.new("RGBA", (1920, 1080))
# new.paste(stage.resize((1920, 1080)), (0, 0))
# new.alpha_composite(back1)
# new.paste(w1.resize((480, 480)), (480*0, 1080-480), w1.resize((480, 480)))
# new.paste(w2.resize((480, 480)), (480*1, 1080-480), w2.resize((480, 480)))
# new.paste(w3.resize((480, 480)), (480*2, 1080-480), w3.resize((480, 480)))
# new.paste(w4.resize((480, 480)), (480*3, 1080-480), w4.resize((480, 480)))
# with open('1.png', 'wb') as f:
#     new.save(f, 'png')