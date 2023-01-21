from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title('open file')

# root.file_name = filedialog.askopenfilename(initialdir="/Users/project_test_image", title="Select A File", filetype=(("png file"), ("*.png"), ("all file", "*.*")))

# my_lable = Label(root, text="filename").pack()

# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_lable = Label(image=my_image).pack()

def open():
     global my_image
     root.filename = filedialog.askopenfilename(initialdir="/Users/project_test_image", title="Select A File", filetype=(("jpg file"), ("* .jpg"), ("all file", "* .*")))
     my_lable = Label(root, text="filename").pack()
     my_image = ImageTk.PhotoImage(Image.open(root.filename))
     my_image_lable = Label(image=my_image).pack()

my_button = Button(root, text="Open File", command=open).pack()
mainloop()