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

    def get_merged_image(self, stage_name, weapon_names):
        # prepare materials
        images = self.get_original_images()
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
            resized_weapon = weapons[index].resize((270, 270))
            merged_image.paste(resized_weapon, (1920-270, 270*index), resized_weapon)

        save_path = 'merged_image.png'
        with open(save_path, 'wb') as f:
            merged_image.save(f, 'png')

        return save_path
