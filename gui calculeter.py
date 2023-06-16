from tkinter import *
screen=Tk()
screen.geometry("400x480")
screen.title("grade Calculeter")

# button Function
def calculate ():
    eng_marks=int(Eng_Entry.get())
    hindi_marks=int(hindi_Entry.get())
    math_marks=int(math_Entry.get())
    science_marks=int(Science_Entry.get())
    sst_marks=int(sst_Entry.get())
    sanskirat_marks=int(Sanskirat_Entry.get())
    total=(eng_marks+hindi_marks+math_marks+science_marks+sst_marks+sanskirat_marks)
    avrage=int(total/6)
    Label(screen,text=total,font="impack 15 bold",).place(x=190,y=280)
    Label(screen,text=avrage,font="impack 15 bold",).place(x=190,y=310)
    Label(screen,text="Total",font=("impack 13  bold")).place(x=30,y=280)
    Label(screen,text="Avrage",font=("impack 13  bold")).place(x=30,y=315)
    Label(screen,text="Grade",font=("impack 13  bold")).place(x=30,y=350)
    if avrage>40:
        grade="pass"
        Label(screen,text=grade,font="impack 15 bold",fg="green").place(x=190,y=345)

    else:
        grade="fall"
        Label(screen,text=grade,font="impack 15 bold",fg="red").place(x=190,y=345)



    

#Heading#
Label(screen,text="Grade Calculator",font=("impack 20 bold"),bg="purple",fg="white").pack(fill=X)
#subjects
Label(screen,text="English",font=("23 ")).place(x=30,y=70)
Label(screen,text="Hindi",font=("23")).place(x=30,y=105)
Label(screen,text="Math",font=("23")).place(x=30,y=140)
Label(screen,text="Science",font=("23")).place(x=30,y=175)
Label(screen,text="S.S.T.",font=("23")).place(x=30,y=210)
Label(screen,text="Sanskirat",font=("23")).place(x=30,y=245)


# Entry #

Eng_Entry=Entry(screen,font="20",bd=2)
Eng_Entry.place(x=180,y=70)
hindi_Entry=Entry(screen,font="20",bd=2)
hindi_Entry.place(x=180,y=105)
math_Entry=Entry(screen,font="20",bd=2)
math_Entry.place(x=180,y=140)
Science_Entry=Entry(screen,font="20",bd=2)
Science_Entry.place(x=180,y=175)
sst_Entry=Entry(screen,font="20",bd=2)
sst_Entry.place(x=180,y=210)
Sanskirat_Entry=Entry(screen,font="20",bd=2)
Sanskirat_Entry.place(x=180,y=245)

#Button#
Button(screen,text="calcluate",font="impack 15 bold ",bg="red",command=calculate).place(x=50,y=390)
Button(screen,text="Exit",font="impack 15 bold ",bg="red",width=8,command=lambda:exit()).place(x=300,y=390)
mainloop()