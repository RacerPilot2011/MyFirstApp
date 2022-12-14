import os, sys,time,sys,tty,os,termios, platform
def exit():
    if platform.system == "Winndows":
        os.system("cls")
        sys.exit()
    else:
        os.system("clear")
        sys.exit()
def clear():
    if platform.system == "Windows":
        os.system("cls")
    else: 
        os.system("clear")
def shell(message):
    os.system(message)
def s(seconds):
    time.sleep(seconds)
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