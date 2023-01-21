from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('New Window')
def open():
    global my_img
    top = Toplevel()
    top.title('AMK Tech')
    my_img =  ImageTk.PhotoImage(Image.open("images/download_1.png"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()


# lbl = Label(top, text="Hello World").pack()

btn = Button(root, text="Open Second Window", command= open).pack()

mainloop()