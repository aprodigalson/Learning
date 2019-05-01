import os
from PIL import Image

ext = ['jpg', 'jpeg', 'png']
files = os.listdir('.')


def process_image(filename, min_width=640, min_height=1136):
    image = Image.open(filename)
    w, h = image.size
    if w <= min_width and h <= min_height:
        return
    if 1.0*w/min_width > 1.0*h/min_height:
        scale = 1.0*w/min_width
        new_image = image.resize((int(w/scale), (int(h/scale))), Image.ANTIALIAS)
    else:
        scale = 1.0*h/min_height
        new_image = image.resize((int(w/scale), (int(h/scale))), Image.ANTIALIAS)
    new_image.save('new_'+filename)
    new_image.close()


for file in files:
    if file.split('.')[-1] in ext:
        process_image(file)
