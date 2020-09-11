import tkinter as tk
from tkinter import messagebox

class Menu:
    def __init__(self,master):
        self.master=master
        f1=tk.Frame(self.master).pack()
        f2=tk.Frame(f1)
        l1a=tk.Label(f2,text="name")
        l1a.grid(row=0,column=0)
        e1a=tk.Entry(f2)
        e1a.grid(row=0,column=1)
        l1b=tk.Label(f2,text="tel")
        l1b.grid(row=1,column=0)
        e1b=tk.Entry(f2)
        e1b.grid(row=1,column=1)
        f2.pack()
        f3=tk.Frame(self.master)
        b1=tk.Button(f3,text="open",command=self.show_msg)
        b1.pack(side=tk.LEFT)
        b2=tk.Button(f3,text="quit",command=root.destroy)
        b2.pack(side=tk.LEFT)
        f3.pack()
    def show_msg(self):
        name=self.master(e1a.get())
        messagebox.showinfo("show info",name)

root=tk.Tk()
root.title("memo")
app=Menu(root)
root.mainloop()
