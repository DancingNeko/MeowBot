from PIL import Image
import PIL
import requests
import random, sys
class Image2Braille:
    def convert(width, sens, file):
        average = lambda x: sum(x)/len(x) if len(x) > 0 else 0
        start = 0x2800
        filename = file
        base = Image.open(requests.get(filename, stream=True).raw)
        char_width = base.width//width
        char_height = char_width * 2
        dither = 10
        sensitivity = sens
        char_width_divided = round(char_width / 2)
        char_height_divided = round(char_height / 4)
        match = lambda a, b: a < b if "--invert" in sys.argv else a > b
        def image_average(x1, y1, x2, y2):
            return average([average(base.getpixel((x, y))[:3]) for x in range(x1, x2) for y in range(y1, y2)])
        def convert_index(x):
            return {3: 6, 4: 3, 5: 4, 6: 5}.get(x, x)
        chrArr = []
        for y in range(0, base.height - char_height - 1, char_height):
            chrStr = ''
            for x in range(0, base.width - char_width - 1, char_width):
                byte = 0x0
                index = 0
                for xn in range(2):
                    for yn in range(4):
                        avg = image_average(x + (char_height_divided * xn), y + (char_width_divided * yn), x + (char_height_divided * (xn + 1)), y + (char_width_divided * (yn + 1)))
                        if match(avg + random.randint(-dither, dither), sensitivity * 0xFF):
                            byte += 2**convert_index(index)
                        index += 1
                chrStr = chrStr + chr(start + byte)
            chrArr.append(chrStr)
        return chrArr