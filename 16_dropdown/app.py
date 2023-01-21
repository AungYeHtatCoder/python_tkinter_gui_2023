from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('Checkbox')
root.geometry("400x400")
def show():
    my_label = Label(root, text=clicked.get()).pack()

options = [
 "Monday", 
 "TueDay",
 "Wedenday", 
 "Thursday", 
 "Friday",
 "Saturday"
]
clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()

my_Button = Button(root, text="show Selectioin", command=show).pack()

mainloop()