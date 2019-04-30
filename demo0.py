from PIL import Image, ImageFont, ImageDraw

# open the file
filename = "touxiang.jpeg"
im = Image.open(filename)
# set font according to platform
fontPath = "/usr/share/fonts/truetype/"
fontSize = int(min(im.size)/10)
font = ImageFont.truetype(font=fontPath+"fonts-japanese-gothic.ttf",size=fontSize)
width, height = im.size
# draw text in canvas
draw = ImageDraw.Draw(im)
text = "1"
draw.text(xy=(width-fontSize*len(text), 0), text=text,fill=(255,0,0),font=font)
# save image
saveName = "test.jpeg"
im.save(saveName)
