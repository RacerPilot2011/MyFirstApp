
import random
import platform
import time
from shortcut import *
def future():
    if platform.system == "Windows":
        w()
    else:
        mal()
    print("\nWelcome to the future telling program!")
    time.sleep(1)
    told()
def told():
    i = 0
    while (i < 3):
        input('What do you want to be fortold\n')
        print("Seeing the future...")
        time.sleep(2)
        determiner = random.randint(1,3)
        if determiner == 1:
            print('My sources say yes')
        elif determiner == 2:
            print('Sorry, no')
        else:
            print('The future is foggy, try again later')
    
    
        if i ==  0:
            print("2 more futures left")
        if i ==  1:
            print("1 more future left")
        if i ==  2:
            print("All futures fortold.")
        time.sleep(1)
        print("Exiting...")
        time.sleep(2)
        if platform.system == "Windows":
            exitw()
        else:
            exitmal()
        i = i + 1
    