import os
import unittest
import datetime

from PIL import Image

from twitter_bot.modules.image_handler import ImageHandler

GROUND_TRUTH = {'start_time': datetime.datetime(2018, 8, 21, 21),
                'end_time': datetime.datetime(2018, 8, 23, 3),
                'weapon1_en': 'Splattershot',
                'weapon1_jp': 'スプラシューター',
                'weapon2_en': 'Slosher',
                'weapon2_jp': 'バケットスロッシャー',
                'weapon3_en': 'Octobrush',
                'weapon3_jp': 'ホクサイ',
                'weapon4_en': 'E-liter 4K Scope',
                'weapon4_jp': '4Kスコープ',
                'stage_en': 'Salmonid Smokeyard',
                'stage_jp': 'トキシラズいぶし工房'}


class ImageHandlerTests(unittest.TestCase):
    def setUp(self):
        self.image_handler = ImageHandler('images')

    def tearDown(self):
        del self.image_handler

    def test_get_original_images(self):
        wanted_result = {'Salmonid Smokeyard': 'images/Salmonid Smokeyard.png',
                         'E-liter 4K Scope': 'images/E-liter 4K Scope.png',
                         'Octobrush': 'images/Octobrush.png',
                         'Slosher': 'images/Slosher.png',
                         'Splattershot': 'images/Splattershot.png',
                         'mask': 'images/mask.png',
                         'sample_image': 'images/sample_image.png'}
        image_list = self.image_handler.get_original_images()
        self.assertDictEqual(wanted_result, image_list)

    def test_get_merged_image(self):
        wanted_result = Image.open('images/sample_image.png')
        schedule = GROUND_TRUTH
        merged_image = self.image_handler.get_merged_image(schedule)
        merged_image = Image.open(merged_image)
        self.assertEqual(wanted_result.histogram(), merged_image.histogram())
        if os.path.exists('images/sample_image.png'):
            os.remove('merged_image.png')


if __name__ == '__main__':
    unittest.main(verbosity=2)
