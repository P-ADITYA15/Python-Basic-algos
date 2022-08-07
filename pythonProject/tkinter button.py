from tkinter import*
t =Tk()
e  =Entry(t,width=20,borderwidth=3,fg="yellow",bg="blue")

e.pack()
def a():
    l = Label(t,text=e.get())
    l.pack()
b = Button(t,text = "click me",command=a,padx=10,pady=10,bg="black",fg="white")
b.pack()
t.mainloop()