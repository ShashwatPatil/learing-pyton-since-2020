
from tkinter import *


def text():
    tx1 = Label(root, text="SUCCESS!!!!", fg="red", bg="blue").pack()


root = Tk()

butt1 = Button(root, text="CLICK ME \n !!!!!!", fg="white", bg="green", padx=50, pady=30, command=text)
butt2 = Button(root, text="TRY TO CLICK ME", state=DISABLED).pack()

butt1.pack()

root.mainloop()
