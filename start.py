import time
import os
import platform
import curses, time
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
    if platform.system == "Windows":
        os.system("python3 index.py")
    else:
        os.system("sudo python3 index.py")

