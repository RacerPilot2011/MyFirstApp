import  os, time 
from shortcut import *
clear()
print("Welcome to my python projects!")
s(2)
print("Do you want to use the [C]oder, play the [G]uessing Game, or ask the [F]uture Teller?")
while True:
    k = getkey()
    if k == 'c':
        a = "aa"
    if k == 'f':
        a = "a"
    if a == "aa":
        shell("python3 cal.py")
    elif a == "a":
        shell("python3 future.py")
