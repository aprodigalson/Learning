from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import string


def get_random_char():
    return random.choice(string.ascii_letters+string.digits)


def get_background_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def get_font_color():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def process():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font_path = "/usr/share/fonts/truetype/"
    font = ImageFont.truetype(font=font_path + "fonts-japanese-gothic.ttf", size=36)
    draw = ImageDraw.Draw(image)
    code = ''
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=get_background_color())
    for i in range(4):
        temp = get_random_char()
        print(temp)
        draw.text((i*60+10, 10), temp, font=font, fill=get_font_color())
        code += temp
    image = image.filter(ImageFilter.BLUR)
    image.save("code.jpg", 'jpeg')


process()
