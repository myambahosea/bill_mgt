from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("RESTAURANT BILL MANAGEMENT SYSTEM")
root.resizable(False, False)

def Reset():
    entry_Rice.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_Pancakes.delete(0,END)
    entry_Eggs.delete(0,END)

def Total():
    try:a1=int(Rice.get())
    except:a1=0

    try:a2=int(Cookies.get())
    except:a2=0

    try:a3=int(Tea.get())
    except:a3=0

    try:a4=int(Coffee.get())
    except:a4=0

    try:a5=int(Juice.get())
    except:a5=0

    try:a6=int(Pancakes.get())
    except:a6=0

    try:a7=int(Eggs.get())
    except:a7=0

    #Define cost of each item per quantity.
    c1=5000*a1
    c2=1000*a2
    c3=700*a3
    c4=2000*a4
    c5=2500*a5
    c6=10000*a6
    c7=500*a7

    lbl_Total = Label(f2, font=("arial", 20, "bold"), text="Total", width=16, fg="lightyellow", bg="black")
    lbl_Total.place(x=0, y=50)

    entry_Total = Entry(f2, font=("arial", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
    entry_Total.place(x=20, y=100)

    Total_cost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Tsh.",str("%.2f" %Total_cost)
    Total_bill.set(string_bill)


Label(text="RESTAURANT BILL MANAGEMENT SYSTEM", bg="black", fg="white", font=("calibri",33), width="300", height="2").pack()

#MENU CARD
f=Frame(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=115)

Label(f, text="Menu", font=("Gabriola", 40,"bold"), fg="black", bg="lightgreen").place(x=100,y=0)

Label(f, font=("Lucida Calligraphy",12,"bold"), text="Rice.......5000Tsh/plate",fg="black", bg="lightgreen").place(x=10,y=80)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Cookies.......1000Tsh/plate",fg="black", bg="lightgreen").place(x=10,y=110)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Tea.......700Tsh/cup",fg="black", bg="lightgreen").place(x=10,y=140)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Coffee......2000Tsh/cup",fg="black", bg="lightgreen").place(x=10,y=170)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Juice.......2500Tsh/glass",fg="black", bg="lightgreen").place(x=10,y=200)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Pancakes.......10000Tsh/pack",fg="black", bg="lightgreen").place(x=10,y=230)
Label(f, font=("Lucida Calligraphy",12,"bold"), text="Eggs.......500Tsh/egg",fg="black", bg="lightgreen").place(x=10,y=260)

#BILL
f2=Frame(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=115)

Bill= Label(f2, text="Bill", font=("calibri",20), bg="lightyellow")
Bill.place(x=120, y=10)

#ENTRY WORK
f1= Frame(root, bd=5, height=370, width=300, relief=RAISED)
f1.pack()

Rice=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pancakes=StringVar()
Eggs=StringVar()
Total_bill=StringVar()

#LABEL
lbl_Rice= Label(f1, font=("arial",20,"bold"), text="Rice", width=12, fg="blue4")
lbl_Cookies= Label(f1, font=("arial",20,"bold"), text="Cookies", width=12, fg="blue4")
lbl_Tea= Label(f1, font=("arial",20,"bold"), text="Tea", width=12, fg="blue4")
lbl_Coffee= Label(f1, font=("arial",20,"bold"), text="Coffee", width=12, fg="blue4")
lbl_Juice= Label(f1, font=("arial",20,"bold"), text="Juice", width=12, fg="blue4")
lbl_Pancakes= Label(f1, font=("arial",20,"bold"), text="Pancakes", width=12, fg="blue4")
lbl_Eggs= Label(f1, font=("arial",20,"bold"), text="Eggs", width=12, fg="blue4")

lbl_Rice.grid(row=1, column=0)
lbl_Cookies.grid(row=2, column=0)
lbl_Tea.grid(row=3, column=0)
lbl_Coffee.grid(row=4, column=0)
lbl_Juice.grid(row=5, column=0)
lbl_Pancakes.grid(row=6, column=0)
lbl_Eggs.grid(row=7, column=0)

#ENTRY
entry_Rice=Entry(f1, font=("arial",20,"bold"), textvariable=Rice, width=8, bg="lightpink")
entry_Cookies=Entry(f1, font=("arial",20,"bold"), textvariable=Cookies, width=8, bg="lightpink")
entry_Tea=Entry(f1, font=("arial",20,"bold"), textvariable=Tea, width=8, bg="lightpink")
entry_Coffee=Entry(f1, font=("arial",20,"bold"), textvariable=Coffee, width=8, bg="lightpink")
entry_Juice=Entry(f1, font=("arial",20,"bold"), textvariable=Juice, width=8, bg="lightpink")
entry_Pancakes=Entry(f1, font=("arial",20,"bold"), textvariable=Pancakes, width=8, bg="lightpink")
entry_Eggs=Entry(f1, font=("arial",20,"bold"), textvariable=Eggs, width=8, bg="lightpink")

entry_Rice.grid(row=1, column=1)
entry_Cookies.grid(row=2, column=1)
entry_Tea.grid(row=3, column=1)
entry_Coffee.grid(row=4, column=1)
entry_Juice.grid(row=5, column=1)
entry_Pancakes.grid(row=6, column=1)
entry_Eggs.grid(row=7, column=1)

#BUTTONS
btn_reset= Button(f1,bd=5, fg="black", bg="lightblue", font=("ariel",16,"bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=8, column=0)

btn_Total= Button(f1,bd=5, fg="black", bg="lightblue", font=("ariel",16,"bold"), width=10, text="Total", command=Total)
btn_Total.grid(row=8, column=1)


root.mainloop()