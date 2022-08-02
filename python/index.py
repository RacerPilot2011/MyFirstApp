import time, keyboard
from future import start

print("Welcome to my python projects!")
time.sleep(1)
print("Do you want to use the [C]alculator, play the [G]uessing Game, or ask the [F]uture Teller?")
if keyboard.read_key() == "f":
    start()