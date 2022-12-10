import time
import os
import platform
import curses, time
try:
    os.system("go version")
    os.system("clear")
except os.error:
    print("Your Are Missing Golang 1.19.3")
    time.sleep(2)
    print("Installing...")
    if platform.system() == "Linux":
        os.chdir("assets")
        os.system("./golang-linux.sh")

def char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        ch = win.getch()
    finally:
        curses.endwin()
    return chr(ch)

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear") 
print("Weclome to all my Programs")
time.sleep(1)
c = char("Do you want to do the [P]ython scripts, [J]ava scripts, [G]olang scripts, or [C]++ scripts(press the key on keyboard.)\n")
if c.lower() in ['p']:
    os.chdir("python")
    print("\nRunning python...")
    time.sleep(1)
    os.system("python3 index.py")
if c.lower() in ['g']:
    os.chdir("golang")
    print("Running golang...")
    time.sleep(1)
    os.system("go run main.go")
