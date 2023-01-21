from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('Checkbox')
root.geometry("400x400")
def show():
    my_lable = Label(root, text=var.get()).pack()

var = IntVar()

c = Checkbutton(root, text="Check this box", variable=var)
c.pack()

my_button = Button(root, text="show Slection", command=show).pack()

mainloop()