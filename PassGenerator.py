from tkinter import *
import random
import string
window=Tk()
window.title("Password Generator App")
window.geometry("800x600+400+80")
window.resizable(False,False)

#functions
def generate_password():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    x = int(E2.get())
    password = ''.join(random.choice(char) for i in range(x))
    E3.insert(END,password)
def reset_password():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    x = int(E2.get())
    password = ''.join(random.choice(char) for i in range(x))
    E3.delete(0, "end")
    E3.insert(END, password)
def accept():
    b=E1.get()
    y=E3.get()
    z="Hello "+b+","+" Your Password is : "+y
    L4.config(text=z)

#design
window.title("Password Generator App")
L=Label(window,text="Password Generator App",font=('Helvetica bold', 26,"bold italic"),fg="Navy")
L.pack()
L1=Label(window,text="Enter User Name :-",font=("arial",15))
L1.pack(padx=(0,595),pady=(30,0))
E1=Entry(window,bd=0.5,highlightthickness=2)
E1.config(highlightbackground = "grey", highlightcolor= "grey",width=40,font=("Helvetica", "14"))
E1.pack(padx =(0,310),pady=(10))
L2=Label(window,text="Enter Password Length :- (Number Only!!!)",font=("arial",15))
L2.pack(padx=(0,390),pady=(0,10))
E2=Entry(window,bd=0.5,highlightthickness=2)
E2.config(highlightbackground = "grey", highlightcolor= "grey",width=40,font=("Helvetica", "14"))
E2.pack(padx =(0,310),pady=(10))
L3=Label(window,text="Generated Password :-",font=("arial",15))
L3.pack(padx=(0,555),pady=(10,0))
E3=Entry(window,bd=0.5,highlightthickness=2)
E3.config(highlightbackground = "grey", highlightcolor= "grey",width=40,font=("Helvetica", "14"))
E3.pack(padx =(0,310),pady=(10))
B1=Button(window,text="Generate Password",width=17,border=0,bg="Navy",font=("Helvetica", "12"),fg="white",command=generate_password)
B1.pack(pady=(20,0))
B2=Button(window,text="Accept",width=17,border=0,bg="Navy",font=("Helvetica", "12"),fg="white",command=accept)
B2.pack(pady=(20,0))
B3=Button(window,text="Reset",width=17,border=0,bg="Navy",font=("Helvetica", "12"),fg="white",command=reset_password)
B3.pack(pady=(20,0))
L4=Label(window,font=("Helvetica", "12"))
L4.pack(pady=(10,0))
window.mainloop()