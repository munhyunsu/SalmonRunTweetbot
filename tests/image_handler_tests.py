import unittest

from PIL import Image

from image_handler import ImageHandler


class ImageHandlerTests(unittest.TestCase):
    """How test this module?
    """
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
                         'mask': 'images/mask.png'}
        image_list = self.image_handler.get_original_images()
        self.assertDictEqual(wanted_result, image_list)

    def test_get_merged_image(self):
        wanted_result = Image.open('image_sample.png')
        stage = 'Salmonid Smokeyard'
        weapons = ['E-liter 4K Scope', 'Octobrush', 'Slosher', 'Splattershot']
        merged_image = self.image_handler.get_merged_image(stage, weapons)
        merged_image = Image.open(merged_image)
        self.assertEqual(wanted_result.histogram(), merged_image.histogram())


if __name__ == '__main__':
    unittest.main(verbosity=2)

# from PIL import Image
#
# stage = Image.open('images/Salmonid Smokeyard.png')
# w1 = Image.open('images/E-liter 4K Scope.png')
# w2 = Image.open('images/Octobrush.png')
# w3 = Image.open('images/Slosher.png')
# w4 = Image.open('images/Splattershot.png')
# back1 = Image.open('images/white1.png')
# back2 = Image.open('images/white2.png')
# back3 = Image.open('images/white3.png')
#
#
# new = Image.new("RGBA", (1920, 1080))
# new.paste(stage.resize((1920, 1080)), (0, 0))
# new.alpha_composite(back1)
# new.paste(w1.resize((480, 480)), (480*0, 1080-480), w1.resize((480, 480)))
# new.paste(w2.resize((480, 480)), (480*1, 1080-480), w2.resize((480, 480)))
# new.paste(w3.resize((480, 480)), (480*2, 1080-480), w3.resize((480, 480)))
# new.paste(w4.resize((480, 480)), (480*3, 1080-480), w4.resize((480, 480)))
# with open('1.png', 'wb') as f:
#     new.save(f, 'png')
#
#
# new = Image.new("RGBA", (1920, 1080))
# new.paste(stage.resize((1920, 1080)), (0, 0))
# new.alpha_composite(back2)
# new.paste(w1.resize((270, 270)), (1920-270, 270*0), w1.resize((270, 270)))
# new.paste(w2.resize((270, 270)), (1920-270, 270*1), w2.resize((270, 270)))
# new.paste(w3.resize((270, 270)), (1920-270, 270*2), w3.resize((270, 270)))
# new.paste(w4.resize((270, 270)), (1920-270, 270*3), w4.resize((270, 270)))
# with open('2.png', 'wb') as f:
#     new.save(f, 'png')
#
#
# new = Image.new("RGBA", (1920, 1080))
# new.paste(stage.resize((1920, 1080)), (0, 0))
# new.alpha_composite(back3)
# new.paste(w1.resize((540, 540)), (1920-540*2, 540*0), w1.resize((540, 540)))
# new.paste(w2.resize((540, 540)), (1920-540*1, 540*0), w2.resize((540, 540)))
# new.paste(w3.resize((540, 540)), (1920-540*2, 540*1), w3.resize((540, 540)))
# new.paste(w4.resize((540, 540)), (1920-540*1, 540*1), w4.resize((540, 540)))
# with open('3.png', 'wb') as f:
#     new.save(f, 'png')