from tkinter import *

# create the root window
root = Tk()
def myClick():
 myLabel = Label(root, text="Look! I clicked a Button!!")
 myLabel.pack()
# create Button
# myButton = Button(root, text="Click Me!", state=DISABLED)
myButton = Button(root, text="Click Me!", padx=50, pady=50, command=myClick, fg="blue", bg="red")
# myButton = Button(root, text="Click Me!", padx=50, pady=50, command=root.quit, fg="blue", bg="red")

# show it on to the screen
myButton.pack()

# run the main event loop
root.mainloop()
