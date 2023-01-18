import random
import sys
from pyfiglet import Figlet
figlet = Figlet()

listf = figlet.getFonts()

if len(sys.argv) == 1:
    word = input("Input: ")
    font = random.choice(listf)
    figlet.setFont(font = font)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in listf:
    word = input("Input: ")
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid Usage")

print(figlet.renderText(word))