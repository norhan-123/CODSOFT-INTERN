from tkinter import *
window=Tk()
window.resizable(0,True)
window.title("To Do List App")
window.geometry("800x800+400+5")
#Functions
def add_task():
    mission=E1.get()
    warning = "empty task, please edit or delete"
    if mission!="":
        L1.insert(END, mission)
        E1.delete(0,"end")
    else:
        L1.insert(END,warning)
def delete():
    x=L1.curselection()
    L1.delete(x)
def edit():
   new_mission=E1.get()
   x = L1.curselection()
   L1.delete(x)
   L1.insert(x,new_mission)
   E1.delete(0,"end")
def clear():
    L1.delete(0,"end")

#design
L=Label(window,text="To Do List App",font=('Helvetica bold', 26,"bold italic"),bg="light blue",height=3,width=90)
L.pack()
L2=Label(window,text="Add Items",font=('Helvetica bold', 24,"bold"))
L2.pack(padx =(0,600))
E1=Entry(window,bd=0.5,highlightthickness=2)
E1.config(highlightbackground = "grey", highlightcolor= "grey",width=60,font=("Helvetica", "14"))
E1.pack(padx =(0,90),pady=(10))
B1=Button(text="Submit",width=7,border=0,bg="lightblue",font=("Helvetica", "12"),command=add_task)
B1.pack(padx=(650,0),pady=(10,0))
F1=Frame(window,bd=3,width=500,height=280,bg="light blue")
F1.pack(pady=(10))
L1=Listbox(F1,font=("arial",10),width=50,height=25,bg="light blue")
L1.pack(side=LEFT)
B2=Button(text="Delete",width=7,border=0,bg="lightblue",font=("Helvetica", "12"),command=delete)
B2.pack(side=RIGHT,padx=(10,285))
B3=Button(text="Edit",width=7,border=0,bg="lightblue",font=("Helvetica", "12"),command=edit)
B3.pack(side=RIGHT,padx=(10,0))
B4=Button(window,text="Clear",width=7,border=0,bg="lightblue",font=("Helvetica", "12"),command=clear)
B4.pack(side=RIGHT)
window.mainloop()






