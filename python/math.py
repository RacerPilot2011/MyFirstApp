import time,random,os
from shortcut import *
os.system("clear")
print("Welcome to the math fact helper!")
time.sleep(2)
print("You will get a fact between 1 and 12.")
time.sleep(2)
def again():
    print("Do you want to [T]ry again, Choose another [P]thon program, [E]xit the whole program, or Choose a different [L]anguage?")
    s = getkey()
    if s == 't':
        facts()
    elif s == 'p':
        shell("python3 index.py")
    elif s == 'e':
        exit()
    elif s == 'l':
        shell("python3 ~/Documents/MyFirstApp/start.py")
def facts():
  a = random.randint(1, 12)
  o = random.randint(1,4)
  if o == 1:
    op = "+"
  if o == 2:
    op = "-"
  if o == 3:
    op = "x"
  if o == 4:
    op = "÷"
  b = random.randint(1,12)
  ask = "You fact is:\n" + str(a) + str(op) + str(b) + "\n"
  ag = input(ask)
  aa = str(ag)
  an = int(aa)
  aw = 0
  start_time = time.time()
  if o==1:
    aw=a+b
  if o==2:
    aw=a-b
  if o==3:
    aw=a*b
  if o==4:
    aw=a/b
  if an == aw:
    endtime = time.time()
    v = str(endtime - start_time)
    tg = v.replace('e', '0').replace('-', '0')
    c = float(tg)
    print("Good job! You got it correct! Your reaction time was:", c, "seconds!")
    again()
  if an != aw:
    endtime = time.time()
    v = str(endtime - start_time)
    tg = v.replace('e', '0').replace('-', '0')
    c = float(tg)
    print("Nice try. The correct answer was", aw, ". Your reaction time was: ", c, "seconds.")
    again()
facts()