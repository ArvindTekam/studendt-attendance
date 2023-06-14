from tkinter import*
from tkinter import messagebox
screen=Tk()
screen.title("Registration From")
screen.geometry("400x400")
screen.resizable(FALSE,FALSE)

def register():
    Name=Name_info.get()
    age=age_info.get()
    mo=mobile_info.get()
    email=email_info.get()

    if Name=="":
        messagebox.showerror("error","Please Enter Your Name")
    
    elif age=="":
        messagebox.showerror("error","Please Enter Your Age")

    elif mo=="":
        messagebox.showerror("error","Please Enter Your Mobile Number")

    elif email=="":
        messagebox.showerror("error","Please Enter Your Email")

    else:
        Label(screen,text="Registration Sucessfull",font="20",fg="green",).place(x=135,y=285)

    with open(Name+".text","w")as f:
        f.write("Name:"+Name+"\n")
        f.write("Age :"+age+"\n")
        f.write("Mobile NO :"+mo+"\n")
        f.write("Email :"+email+"\n")
def clear():
    name_Entry.delete(0,END)
    Age_Entry.delete(0,END)
    mobile_Entry.delete(0,END)
    Email_Entry.delete(0,END)

# lable
Label(screen,text="Registration From",font=(" aeirl 20 bold "),bg='red',fg='black').pack()
Label(screen,text="Name",font=(" 20 ")).place(x=30,y=70)
Label(screen,text="Age",font=(" 20 ")).place(x=30,y=110)
Label(screen,text="Mobile No.",font=(" 20 ")).place(x=30,y=150)
Label(screen,text="Email",font=(" 20 ")).place(x=30,y=190)

# Entry
Name_info=StringVar()
age_info=StringVar()
mobile_info=StringVar()
email_info=StringVar()

name_Entry=Entry(screen,font="10",bd=4,textvariable=Name_info)
name_Entry.place(x=140,y=70)

Age_Entry=Entry(screen,font="10",bd=4,textvariable=age_info)
Age_Entry.place(x=140,y=110)

mobile_Entry=Entry(screen,font="10",bd=4,textvariable=mobile_info)
mobile_Entry.place(x=140,y=150)

Email_Entry=Entry(screen,font="10",bd=4,textvariable=email_info)
Email_Entry.place(x=140,y=190)

# button
b=Button(screen,text="Register",font=('20'),command=register).place(x=185,y=255)
c=Button(screen,text="Clear",font=('20'),command=clear).place(x=345,y=365)

mainloop()