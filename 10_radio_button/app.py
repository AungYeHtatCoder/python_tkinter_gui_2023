from tkinter import * 

from PIL import ImageTk, Image

root = Tk()

root.title('Learn to code at AMK Tech')

# r = IntVar()
# r.set("2")
# r.get()


# python list
MODES =  [
 ("Pepperoni", "Pepperoni"),
 ("Cheese", "Cheese"),
 ("Mushroom", "Mushroom"),
 ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)
def clicked(value):
    myLabel = Label(root, text=value).pack()
    
# Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()

# Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()


# myLabel = Label(root, text=r.get()).pack()
# myLabel = Label(root, text=pizza.get()).pack()

# myLabel.pack()
myButton = Button(root, text='Click Me', command=lambda: clicked(pizza.get())).pack()
root.mainloop()