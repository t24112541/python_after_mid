import tkinter as tk
class window1:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.btn_1=tk.Button(self.frame,text="new window",width=25,command=self.new_window)
        self.btn_1.pack()
        self.frame.pack()
    def new_window(self):
        self.newWindow=tk.Toplevel(self.master)
        self.app=window2(self.newWindow)
class window2:
    def __init__(self,master):
        self.master=master
        self.frame=tk.Frame(self.master)
        self.btn_quit=tk.Button(self.master,text="quit",width=25,command=self.close_window)
        self.btn_quit.pack()
        self.frame.pack()
    def close_window(self):
        self.master.destroy()

def main():
    root=tk.Tk()
    app=window1(root)
    root.mainloop()

if __name__=='__main__':
    main()
