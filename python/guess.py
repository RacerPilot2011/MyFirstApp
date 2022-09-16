import platform, random
from shortcut import *
from getch import char
import sys
def gues():
    if platform.system == "Windows":
        w()
    else :
        mal()
    print("\nWelcome to the guessing the number game!")
    s(2)
    print("Guess a number between 1 and 100.")
    s(2)
    i = 0
    n = random.randint(1,100)
    while(i<2):
        guess = input('What is you guess?\n')
        g = int(guess)
        if g == n:
            print("You guessed the number!")
            break
        elif g < n:
            print("Less than.")
        elif g > n:
            print("Greater than.")
    c = char('Do you want to [p]lay again, [e]xit the whole program, choose another program [s]ame launguage, or another program [d]ifferent lanuage?\n')
    if c.lower() in ['p']:
        gues()
    if c.lower() in ['s']:
        shell("python3 index.py")
    if c.lower() in ['e']:
        if platform.system == "Windows":
            exitw()
        else:
            exitmal()
    if c.lower() in ['d']:
        if platform.system == "Windows":
            os.chdir("%USERPROFILE%/Documents/MyFirstApp-main")
            shell("python3 start.py")
        else:
            sys.path.append("/~/Documents/MyFirstApp-main")
            shell("python3 start.py")
gues()