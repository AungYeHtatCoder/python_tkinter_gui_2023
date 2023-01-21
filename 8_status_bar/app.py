from tkinter import * 
from PIL import ImageTk, Image 
root = Tk()
root.title("AMK Tech")
# root.iconbitmap("icob.png")

my_img_1 = ImageTk.PhotoImage(Image.open("img/download_1.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("img/download_2.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("img/download_3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("img/download_4.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("img/download_5.png"))


img_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

status = Label(root, text="Image 1 of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
 global my_label
 global button_forward
 global button_back
 my_label.grid_forget()
 my_label = Label(image=img_list[image_number-1])
 button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
 button_back = Button(root, text="<<", command=lambda: back(image_number-1))
 if image_number == 5:
  button_forward = Button(root, text=">>", state=DISABLED)
 my_label.grid(row=0, column=0, columnspan=3)
 button_back.grid(row=1, column=0)
 button_forward.grid(row=1, column=2)
 status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
 status.grid(row=2, column=0, columnspan=3, sticky=W+E)
 
 

def back(image_number):
 global my_label
 global button_forward
 global button_back
 
 my_label.grid_forget()
 my_label = Label(image=img_list[image_number-1])
 button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
 button_back = Button(root, text="<<", command=lambda: back(image_number-1))
 
 if image_number == 1:
  button_back = Button(root, text="<<", state=DISABLED)
 my_label.grid(row=0, column=0, columnspan=3)
 button_back.grid(row=1, column=0)
 button_forward.grid(row=1, column=2)
 status = Label(root, text="Image " + str(image_number) + " of " + str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
 status.grid(row=2, column=0, columnspan=3, sticky=W+E)
 
 
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()

 # pip install Pillow
 # pip freeze (to check if pillow is installed)