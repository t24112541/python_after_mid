from tkinter import *
class menu:
    def __init__(self,master):
        self.master=master
        frame=Frame(master)
        Button(frame,text="add",width=25,command=self.win_add).pack()
        Button(frame,text="search by name",width=25,command=self.win_s_name).pack()
        Button(frame,text="search by number",width=25,command=self.win_s_number).pack()
        Button(frame,text="show list",width=25,command=self.win_sh).pack()
        Button(frame,text="exit",width=25,command=master.destroy).pack()
        frame.pack()
    def win_add(self):
        self.new_win=Toplevel(self.master)
        
        self.app=add(self.new_win)
        self.app.master.title("add")
    def win_s_name(self):
        new_win=tk.Toplevel(self.master)
        app=menu2(self.new_win)
    def win_s_number(self):
        new_win=tk.Toplevel(self.master)
        app=menu2(self.new_win)
    def win_sh(self):
        new_win=tk.Toplevel(self.master)
        app=menu2(self.new_win)
class add:
    def __init__(self,master):
        self.master=master
        f1=Frame(self.master)
        Label(f1,text="name:").grid(row=0,column=0)
        self.txt_name=Entry(f1).grid(row=0,column=1)
        Label(f1,text="phone:").grid(row=1,column=0)
        txt_tel=Entry(f1).grid(row=1,column=1)
        f1.pack()
        
        f2=Frame(self.master)
        Button(f2,text="add",command=self.func_add).pack(side=LEFT)
        Button(f2,text="cancel",command=master.destroy).pack(side=LEFT)
        f2.pack()
    def func_add(self):
        print(add.self.txt_name.get())
def main():
    root=Tk()
    root.title("phone book")
    root.geometry("300x150")
    app=menu(root)
    root.mainloop()
if __name__=='__main__':
    main()
