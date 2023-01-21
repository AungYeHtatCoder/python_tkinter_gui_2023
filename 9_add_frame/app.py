from tkinter import * 

from PIL import ImageTk, Image

root = Tk()

root.title('Learn to Code at AMK Tech')


# frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame = LabelFrame(root,  padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't Click Here!")
b_2 = Button(frame, text="...or here")
b.grid(row="0", column="0")
b_2.grid(row="1", column="1")
# b.pack()













root.mainloop()