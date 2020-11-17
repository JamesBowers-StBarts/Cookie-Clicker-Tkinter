from tkinter import *

add_per_second=1
upgrades=[1,5,10,25,50,100,250,500,1000]
costs=[5,10,25,50,100,250,500,1000,5000]

def move_frame(direction_number):
    global current_frame
    current_frame = current_frame + direction_number
    if current_frame == 2:
        current_frame =0
    elif current_frame == -1:
        current_frame =1
    selected_frame = frames_list[current_frame]
    selected_frame.tkraise()

def upgrade_cookie_growth():
    global add_per_second
    global no_of_cookies
    if no_of_cookies>=costs[x]:
        add_per_second=add_per_second+upgrades[y]
        no_of_cookies=no_of_cookies-costs[x]
    else:
        print()

def Add_cookies():
    global no_of_cookies
    global add_per_second
    no_of_cookies = no_of_cookies + add_per_second
    cookies_label.configure(text="cookies: "+str(no_of_cookies))
    cps_label.configure(text="CPS: "+str(add_per_second))
    root.after(1000, Add_cookies)

def Manual_cookie_add():
    global no_of_cookies
    no_of_cookies=no_of_cookies+1
    cookies_label.configure(text="cookies: "+str(no_of_cookies))

root =Tk()

top_frame = Frame(root, bg = "Grey")
top_frame.grid(row=0,column=0,sticky=E+W+S+N)
cookies_label = Label(top_frame,text="hi")
cookies_label.grid(row=1,column=0)
cps_label = Label(top_frame,text="temp")
cps_label.grid(row=1, column=1)
no_of_cookies = 0
Add_cookies()

content_frame2 = Frame(root, bg = "white")
content_frame2.grid(row=1,column=0,sticky=E+W+S+N)
title = Label(content_frame2, text="Upgrades")
upgrade_cookie_growth_button=Button(content_frame2, text="+1 cps (-50)",command=upgrade_cookie_growth)
upgrade_cookie_growth_button.grid(row=2)
title.grid(row=1)

content_frame1 = Frame(root, bg = "black")
content_frame1.grid(row=1,column=0,sticky=E+W+S+N)
manual_cookie_add_button=Button(content_frame1,text="Make a cookie",command=Manual_cookie_add)
manual_cookie_add_button.grid(row=1)

forward_button = Button(top_frame, text="<--",bg = "Grey",fg="white",command = lambda: move_frame(1))
forward_button.grid(row=0,column=0,pady=(10,10),sticky="ESNW")
back_button = Button(top_frame, text="-->",bg = "Grey",fg="white",command = lambda: move_frame(-1))
back_button.grid(row=0,column=1,pady=(10,10),sticky="ESNW")

current_frame = 0
frames_list = [content_frame1,content_frame2]

root.rowconfigure(0,minsize = 100,weight=0)
root.rowconfigure(1,minsize = 400,weight=1)
root.columnconfigure(0,minsize = 500,weight=1)


content_frame1.columnconfigure(0,minsize = 200,weight=1)
content_frame1.rowconfigure(0,minsize = 200)
content_frame2.columnconfigure(0,minsize = 200,weight=1)

root.mainloop()

