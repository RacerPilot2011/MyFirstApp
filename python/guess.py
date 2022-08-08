import time, platform, random
from clear import *
def gues():
    if platform.system == "Windows":
        w()
    else :
        mal()
    print("\nWelcome to the guessing the number game!")
    time.sleep(2)
    print("Guess a number between 1 and 100.")
    time.sleep(2)
    i = 0
    while(i<2):
        guess = input=('What is you guess?\n')
        g = int(guess)
        n = random.randint(1,100)
        print(n)
        if g == n:
            print("You guessed the number!")
            break

