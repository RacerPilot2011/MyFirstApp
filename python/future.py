import random
from shortcut import *
clear()
print("\nWelcome to the future telling program!")
s(1)
told()
def told():
    i = 0
    while (i < 3):
        input('What do you want to be fortold\n')
        print("Seeing the future...")

        determiner = random.randint(1,3)
        if determiner == 1:
            print('My sources say yes')
        elif determiner == 2:
            print('Sorry, no')
        else:
            print('The future is foggy, try again later')
        if i == 0:
            print("2 more futures left to be fortold.")
        elif i == 1:
            print("1 more future left to be for told.")
    s(1)
    print("Exiting...")
    s(2)
    if platform.system == "Windows":
        exitw()
    else:
        exitmal()
    exit()
