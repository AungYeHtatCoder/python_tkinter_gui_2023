from tkinter import *

# create the root window
root = Tk()

# create an input field
input_field = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)

# show it on to the screen
input_field.pack()
input_field.insert(0, "enter Your name: ")
def myClick():
    hello = "Hello " + input_field.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=myClick, fg="blue", bg="white")
myButton.pack()

# run the main event loop
root.mainloop()
