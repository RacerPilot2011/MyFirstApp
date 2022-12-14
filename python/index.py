import  platform
from future import *
from cal import *
from shortcut import *
if platform.system() == "Windows":
    w()
else:
    mal()
print("Welcome to my python projects!")
s(2)
print("Do you want to use the [C]oder, play the [G]uessing Game, or ask the [F]uture Teller?\n")
while True:
    k = getkey()
    if k == 'c':
        a = "aa"
    if k == 'f':
        a = "a"
    if a == "aa":
        edc()
    elif a == "a":
        future()
