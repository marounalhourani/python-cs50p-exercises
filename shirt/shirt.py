import sys
import os.path
from PIL import Image, ImageOps

inp_img = sys.argv[1]
out_img = sys.argv[2]
ext_1 = os.path.splitext(inp_img)
ext_2 = os.path.splitext(out_img)
ext = [".jpg", ".jpeg", ".png"]

if len(sys.argv) < 3:
    sys.exist("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if ext_1[1].lower() not in ext:
    sys.exit("Invalid input")
if ext_2[1].lower() not in ext:
    sys.exit("Invalid output")

if ext_1[1].lower() != ext_2[1].lower():
    sys.exit("Input and output have different extensions")

try:
    imagefile = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirtfile = Image.open("shirt.png")
size = shirtfile.size
muppet = ImageOps.fit(imagefile, size)
muppet.paste(shirtfile, shirtfile)
muppet.save(sys.argv[2])

