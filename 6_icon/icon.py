from tkinter import * 
from PIL import ImageTk, Image 
root = Tk()
root.title("AMK Tech")
root.iconbitmap("icob.png")

my_img = ImageTk.PhotoImage(Image.open("icob.png"))
my_lable = Label(image=my_img)
my_lable.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()


root.mainloop()

 # pip install Pillow
 # pip freeze (to check if pillow is installed)