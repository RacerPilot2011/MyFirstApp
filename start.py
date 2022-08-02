import keyboard
import time
import os
import platform
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear") 
print("Weclome to all my Programs")
time.sleep(1)
print("Do you want to do the [P]ython scripts, [J]ava scripts, [G]olang scripts, or [C]++ scripts(press the key on keyboard.)")
if keyboard.read_key() == "g":
    os.chdir("golang")
    print("Running golang...")
    time.sleep(2)
    os.system("go run main.go")
elif keyboard.read_key() == "p":
    os.chdir("python")
    print("Running python...")
    time.sleep(2)
    if platform.system == "Darwin":
        os.system("sudo python3 index.py")
    else:
        os.system("python3 index.py")
elif keyboard.read_key() == "j":
    os.chdir("java")
    print("Running java...")
    os.system("javac main.java")
    os.system("java main")
elif keyboard.read_key() == "c":
    os.chdir("c++")
    print("Running c++...")
    os.system("g++ main.cpp -o main")
    os.system("./main")
