import sys
#import pyfiglet
import random
from pyfiglet import Figlet

figlet = Figlet()
listf = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(listf)
    figlet.setFont(font = font)
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in listf:
    text = input("Input: ")
    figlet.setFont(font = sys.argv[2])
    print(figlet.renderText(text))
    print()
else:
    sys.exit("Invalid usage")

