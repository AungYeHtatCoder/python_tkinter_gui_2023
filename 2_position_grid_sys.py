from tkinter import *
root = Tk()
# create label widget
myLabel_1 = Label(root, text="Hello World!")
myLabel_2 = Label(root, text="My name is AungMyoKhaing!")

# myLabel_1 = Label(root, text="Hello World!").grid(row=0, column=0)
# myLabel_2 = Label(root, text="My name is AungMyoKhaing!").grid(row=1, column=5)
# myLabel_3 = Label(root, text="")

# show it on to the screen
myLabel_1.grid(row=0, column=0)
myLabel_2.grid(row=1, column=5)
# myLabel_3.grid(row=1, column=1)

root.mainloop()