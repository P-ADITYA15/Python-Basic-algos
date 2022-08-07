from tkinter import *
mw = Tk()
mw.title("hello")
b = PhotoImage(file="C:/Users/Aditya/OneDrive/Desktop/zoro.png")
mw.minsize(width=200,height=200)
mw.maxsize(width=1000,height=800)
d = StringVar()
def f():
    x=d.get()
    h = Label(text=x)
    h.pack()
t = Checkbutton(mw,text ="ad")
t.pack()
a = Label(mw,bg="white",text="h",image=b,width=500,height=500)
c = Button(mw,text="hhhh",bg="black",fg="white",command=f)
e = Entry(mw,width=20,bd=20,textvariable=d)
e.pack()
#a.grid(row=3,column=2)
a.place(x=20,y=200)
c.pack()
l = Listbox()
r = Radiobutton
mw.mainloop()


