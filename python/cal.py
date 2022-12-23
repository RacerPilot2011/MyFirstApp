import pyperclip
from shortcut import *
clear()
print("Coder version 1.0")
s(1)
print("Do you want to [E]ncode or [D]ecode?")
def e():
    d = input('What do you want to encode?\n')
    encode = d.replace('a', '1').replace('b', 'f').replace('c', 'r').replace('d', '@').replace('e', '2').replace(' ', '$').replace('g', '%').replace('h', '[').replace('i', 'T').replace('j', '(').replace('k', 'v').replace('l', '0').replace('m', '>').replace('n', '"')
    print("Your encoded message is :\n",encode, "\nDo you want to copy it?([Y]es/[N]o)")
    while True:
        k = getkey()
        if k == 'y':
            a = "aa"
        if k == 'n':
            a = "a"
        if a == "aa":
            pyperclip.copy(encode)
            if platform.system == "Windows":
                exitw()
            else:
                exitmal()
        elif a == "a":
            if platform.system == "Windows":
                exitw()
            else:
                exitmal()
def d():
    d = input('What do you want to decode?\n')
    decode = d.replace('1', 'a').replace('f', 'b').replace('r', 'c').replace('@', 'd').replace('2', 'e').replace('$', ' ').replace('%', 'g').replace('[', 'h').replace('T', 'i').replace('(', 'j').replace('v', 'k').replace('0', 'l').replace('>', 'm').replace('"', 'n')
    print("Your decoded message is\n",decode,"\nDo you want to copy?([Y]es/[N]o)")
    while True:
        k = getkey()
        if k == 'y':
            a = "aa"
        if k == 'n':
            a = "a"
        if a == "aa":
            pyperclip.copy(decode)
            break
        elif a == "a":
            if platform.system == "Windows":
                exitw()
            else:
                exitmal()
while True:
    k = getkey()
    if k == 'e':
        a = "aa"
        break
    if k == 'd':
        a = "a"
        break
if a == "aa":
    e()
elif a == "a":
    d()

