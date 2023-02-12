from shortcut import clear, getkey,s,shell
clear()
print("Welcome to my python projects!")
s(2)
print("Do you want to use the [C]oder, test out your facts skills with the the [M]ath Game, or ask the [F]uture Teller?")
while True:
    k = getkey()
    if k == 'c':
        shell("python3 ~/Documents/MyFirstApp/python/cal.py")
    elif k == 'f':
        shell("python3 ~/Documents/MyFirstApp/python/future.py")
    elif k == 'm':
        shell("python3 ~/Documents/MyFirstApp/python/math.py")
    
