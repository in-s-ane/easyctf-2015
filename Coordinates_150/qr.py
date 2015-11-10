from PIL import Image

img = Image.new("RGB", (29,29), "black")

WHITE = (255, 255, 255, 255)

coords = eval(open("qr.txt", "r").read())
pixels = img.load()
for (x, y) in coords:
    pixels[x, y] = WHITE

img.save('qr.png')
