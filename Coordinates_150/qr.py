import Image
import ImageDraw
from PIL import Image

img = Image.new("RGB", (30,30), "black")
# draw = ImageDraw.Draw(img)

# dotSize = 1

# for (x,y) in coords:
#     draw.ellipse([x,y,x+dotSize-1,y+dotSize-1], fill="black")

img.save("qr.png")

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 0)

coords = eval(open("qr.txt", "r").read())
def read(img):
    image = Image.open(img)
    pixels = image.load()
    for (x, y) in coords:
        pixels[x, y] = WHITE

    image.save('out.png')

read("qr.png")
