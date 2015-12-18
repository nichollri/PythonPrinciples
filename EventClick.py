#from tkinter import *
import tkinter

root = tkinter.Tk()

def button_callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

def key_callback(event):
    print("pressed", repr(event.char), "key sim:", repr(event.keysym),
          "key code:", repr(event.keycode))

frame = tkinter.Frame(root, width=100, height=100)
frame.bind("<Button-1>", button_callback)
frame.bind("<Key>", key_callback)
frame.pack()

root.mainloop()



