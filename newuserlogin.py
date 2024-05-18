from tkinter import *
from tkinter import messagebox
import sqlite3
import os

root=Tk()
root.geometry("900x900")
root.title("New User Login Screen")

txtname=StringVar()
txtphoneno=StringVar()
txtusername=StringVar()
txtpassword=StringVar()

def create_clicked():
    con = sqlite3.connect("mydatabase.sqlite")
    c = con.cursor()
    n = txtname.get()
    ph = txtphoneno.get()
    u = txtusername.get()
    p = txtpassword.get()
    c.execute("select * FROM newuserlogin where username=?", (u,))
    datalist = c.fetchall()
    
    if len(datalist) > 0:
        messagebox.showinfo("Alert", "Username already exists..")
    else:
        c.execute("INSERT INTO newuserlogin(name, phoneno, username, password) VALUES (?, ?, ?, ?)", (n, ph, u, p))
        con.commit()
        messagebox.showinfo("Congrats", "User Created..")
        
    clear_clicked()
    t1.focus()
    con.close()
    
def exit_clicked():
    root.destroy()

def clear_clicked():
    txtname.set("")
    txtphoneno.set("")
    txtusername.set("")
    txtpassword.set("")

def back_clicked():
    root.destroy()
    os.system("userlogin.py")

l0=Label(root,text="New User Login Screen")
l1=Label(root,text="Enter Name")
l2=Label(root,text="Enter Phone Number")
l3=Label(root,text="Enter Username")
l4=Label(root,text="Enter Password")

t1=Entry(root,textvariable=txtname)
t2=Entry(root,textvariable=txtphoneno)
t3=Entry(root,textvariable=txtusername)
t4=Entry(root,textvariable=txtpassword,show="*")

l0.place(x=150,y=50)
l1.place(x=100,y=150)
l2.place(x=100,y=250)
l3.place(x=100,y=350)
l4.place(x=100,y=450)

t1.place(x=200,y=150)
t2.place(x=200,y=250)
t3.place(x=200,y=350)
t4.place(x=200,y=450)
b0=Button(root,text="Login",command=create_clicked)
b1=Button(root,text="Back",command=back_clicked)
b2=Button(root,text="Clear",command=clear_clicked)
b0.place(x=150,y=550)
b1.place(x=250,y=550)
b2.place(x=350,y=550)
t1.focus()
root.mainloop()

