from tkinter import *
from PIL import ImageTk, Image



def change_visibility(frame_parameter):
    frame_parameter.tkraise()


root =Tk()


top_frame = Frame(root, bg = "Grey")
top_frame.grid(row=0,column=0,sticky=E+W+S+N)

content_frame2 = Frame(root, bg = "white")
content_frame2.grid(row=1,column=0,sticky=E+W+S+N)

content_frame1 = Frame(root, bg = "white")
content_frame1.grid(row=1,column=0,sticky=E+W+S+N)

frame1_button = Button(top_frame, text="Show mole",bg = "Grey",fg="white",command = lambda: change_visibility(content_frame1))
frame1_button.grid(row=0,column=0,pady=(10,10),sticky="ESNW")
frame2_button = Button(top_frame, text="Show crocodile",bg = "Grey",fg="white",command = lambda: change_visibility(content_frame2))
frame2_button.grid(row=0,column=1,pady=(10,10),sticky="ESNW")

#images will only work after Tk() has been called
image_file = Image.open(crock)
image_file = image_file.resize((100, 100), Image.ANTIALIAS)
image1= ImageTk.PhotoImage(image_file)

bottom_label = Label(content_frame1, image=image1,bg = "white",)
bottom_label.grid(row=1,column=0,columnspan=2,pady=(10,10))

root.rowconfigure(0,minsize = 100,weight=0)
root.rowconfigure(1,minsize = 400,weight=1)
root.columnconfigure(0,minsize = 500,weight=1)


content_frame1.columnconfigure(0,minsize = 200,weight=1)
content_frame1.rowconfigure(0,minsize = 200)

root.mainloop()
