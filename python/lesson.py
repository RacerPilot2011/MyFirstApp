
import random
import time

question = input('what is your yes or no question?')
determiner = random.randint(1,4)
if determiner == 1:
    print('My sources say yes')
elif determiner == 2:
    print('Sorry, no')
else:
    print('The future is foggy, try again later')