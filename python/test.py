from tkinter import *
import tkinter.messagebox
root = tkinter.Tk()
def onClick():
	tkinter.messagebox.showinfo("Welcome to GFG.", "Hi I'm your message")
root.title("Starting coder...")
root.geometry('500x300')
button = Button(root, text="Click Me", command=onClick, height=5, width=10)
button.pack(side='bottom')
root.mainloop()