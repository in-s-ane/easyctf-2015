import Image
import ImageDraw
from PIL import Image

img = Image.new("RGB", (29,29), "black")

img.save("black.png")

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)
RED = (255, 0, 0, 0)

coords = eval(open("qr.txt", "r").read())
def read(img):
    image = Image.open(img)
    pixels = image.load()
    for (x, y) in coords:
        pixels[x, y] = WHITE

    image.save('qr.png')

read("black.png")
