import tkinter as tk
class menu:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.btn_1=tk.Button(self.frame,text="new window1",width=25,command=self.new_win1).pack()
        self.btn_2=tk.Button(self.frame,text="new window2",width=25,command=self.new_win2).pack()
        self.btn_quit=tk.Button(self.frame,text="quit",width=25,command=self.close_win).pack()
        self.frame.pack()
    def new_win1(self):
        self.new_win=tk.Toplevel(self.master)
        self.app=menu2(self.new_win)
    def new_win2(self):
        self.new_win=tk.Toplevel(self.master)
        self.app=menu2(self.new_win)
        self.app.master.title("gui 2")
        self.app.master.geometry("250x25")
    def close_win(self):
        self.master.destroy()
class menu2:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.btn_quit=tk.Button(self.frame,text="quit",width=25,command=self.close_win).pack()
        self.frame.pack()
    def close_win(self):
        self.master.destroy()
    def set_caption(self,test):
        self.master.title("test")
def main():
    root=tk.Tk()
    app=menu(root)
    root.mainloop()
if __name__=='__main__':
    main()
