
from tkinter import *

root = Tk()

tx1 = Label(root, text="HELLO WORLD!!!!!!\n !!!!!!!!!!!!")
tx2 = Label(root, text="My name is Shashwat G. Patil")
tx3 = Label(root, text="My \n name is \n Shashwat G. Patil")

tx1.grid(row=0, column=0)
tx2.grid(row=1, column=3)
tx3.grid(row=3, column=2)

root.mainloop()
