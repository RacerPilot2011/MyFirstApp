import termios
import time
import os,sys
import platform
import tty

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
os.system("pip3 install --upgrade pip")
os.system("pip3 install pyperclip")
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
    elif platform.system() == "Windows":
        os.chdir("assets")
        s = os.path.expanduser('~\Documents\MyFirstApp')
        
        os.system(s, "golang-windows.cmd")

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear") 
print("Weclome to all my Programs")
time.sleep(1)
def language():
    print("Do you want to do the [P]ython scripts, [G]olang scripts, or [C]++ scripts(press the key on keyboard.)")
    while True:
        k = getkey()
        if k == 'p':
            a = "aa"
        if a == "aa":
            os.chdir("python")
            print("Running python...")
            time.sleep(1)
            os.system("python3 index.py")
            break
language()