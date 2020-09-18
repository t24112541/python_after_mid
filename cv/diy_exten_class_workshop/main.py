from tkinter import *
from tkinter import messagebox
from data import *
data=dt()
class menu:
    def __init__(self,master):
        self.master=master
        frame=Frame(master)
        Button(frame,text="add",width=55,command=self.win_add).grid(row=0,column=0,columnspan=4)
        Label(frame,text="search").grid(row=1,column=0)
        self.txt_search=Entry(frame)
        self.txt_search.grid(row=1,column=1)
        Button(frame,text="search by name",width=15,command=lambda:self.win_search("name")).grid(row=1,column=2)
        Button(frame,text="search by number",width=15,command=lambda:self.win_search("tel")).grid(row=1,column=3)
        Button(frame,text="show list",width=55,command=self.win_sh).grid(row=5,column=0,columnspan=4)
        Button(frame,text="exit",width=55,command=master.destroy).grid(row=6,column=0,columnspan=4)
        frame.pack()
    def win_add(self):
        self.new_win=Toplevel(self.master)
        self.app=add(self.new_win)
        self.app.master.title("add")
    def win_search(self,target):
        n=data.get_dt_name()
        t=data.get_dt_tel()
        res=""
        
        for i in range(len(n)):
            if target=="name":
                if n[i]==self.txt_search.get():
                    res+="name:"+str(n[i])+"\n tel:"+str(t[i])
            elif target=="tel":
                print(t[i])
                print(self.txt_search.get())
                if t[i]==(self.txt_search.get()):
                    res+="name:"+str(n[i])+"\n tel:"+str(t[i])
        if res!="":
            messagebox.showinfo("search",res)
        else:
            messagebox.showinfo("search","ไม่พบข้อมูล")
        
    def win_sh(self):
        self.new_win=Toplevel(self.master)
        self.app=sh(self.new_win)

class add:
    def __init__(self,master):
        self.master=master
        f1=Frame(self.master)
        Label(f1,text="name:").grid(row=0,column=0)
        self.txt_name=Entry(f1)
        self.txt_name.grid(row=0,column=1)
        Label(f1,text="phone:").grid(row=1,column=0)
        self.txt_tel=Entry(f1)
        self.txt_tel.grid(row=1,column=1)
        f1.pack()
        f2=Frame(self.master)
        Button(f2,text="add",command=self.func_add).pack(side=LEFT)
        Button(f2,text="cancel",command=master.destroy).pack(side=LEFT)
        f2.pack()
    def func_add(self):
        data.add("dt_name",self.txt_name.get())
        stg_2=data.add("dt_tel",self.txt_tel.get())
        if not stg_2:
            messagebox.showerror("error","เบอร์ซ้ำ")
        else:
            messagebox.showinfo("success","เพิ่มข้อมูลสำเร็จ")
class sh:
    def __init__(self,master):
        self.master=master
        f2=Frame(self.master)
        scb=Scrollbar(f2)
        scb.pack(side=RIGHT,fill=Y)
        self.lst_1=Listbox(f2,yscrollcommand=scb.set,selectmode=SINGLE)
        scb.config(command=self.lst_1.yview)
        n=data.get_dt_name()
        t=data.get_dt_tel()

        for i in range(len(n)):
            self.lst_1.insert(END,str(n[i])+"   "+str(t[i]))
        self.lst_1.pack(fill=BOTH)
        f2.pack()
def main():
    root=Tk()
    print(data.get_dt_name())
    root.title("phone book")
    root.geometry("500x120")
    app=menu(root)
    root.mainloop()
if __name__=='__main__':
    main()
