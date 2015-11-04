import Image
import ImageDraw

img = Image.new("RGB", (50,50), "white")
draw = ImageDraw.Draw(img)

coords = eval(open("qr.txt", "r").read())
dotSize = 1

for (x,y) in coords:
    draw.rectangle([x,y,x+dotSize-1,y+dotSize-1], fill="black")

img.save("qr.png")
