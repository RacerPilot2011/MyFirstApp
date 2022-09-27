from getch import *
from shortcut import *
import platform
def edc():
    if platform.system == "Windows ":
        w()
    else:
        mal()
    print("Coder version 1.0")
    def e():
        d = input('What do you want to encode?\n')
        print(d.replace('a', '1').replace('b', 'f').replace('c', 'r').replace('d', '@').replace('e', '2').replace('f', ' ').replace('g', '%').replace('h', '[').replace('i', 'T').replace('j', '(').replace('k', 'v').replace('l', '0').replace('m', '>').replace('n', '"'))
    def d():
        d = input('What do you want to decode?\n')
        print(d.replace('1', 'a').replace('f', 'b').replace('r', 'c').replace('@', 'd').replace('2', 'e').replace(' ', 'f').replace('%', 'g').replace('[', 'h').replace('T', 'i').replace('(', 'j').replace('v', 'k').replace('0', 'l').replace('>', 'm').replace('"', 'n'))
edc()
