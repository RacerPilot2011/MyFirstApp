import  platform
from future import *
from guess import *
from shortcut import w,mal,s
from getch import char
if platform.system() == "Windows":
    w()
else:
    mal()
print("Welcome to my python projects!")
s(2)
c = char("Do you want to use the [C]alculator, play the [G]uessing Game, or ask the [F]uture Teller?\n")
if c.lower() in ['f']:
    future()
if c.lower() in ['g']:
    gues()
