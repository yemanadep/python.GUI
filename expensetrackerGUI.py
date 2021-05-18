from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import sqlite3

root=Tk()
root.title("Expense Tracker")
root.geometry("600x400")
#root.resizable(0,0)
#root.config(bg="black")
EDateE, ETitleE, EExpenseE, TVExpense = "" , "", "", ""

EDateI, ETitleI, EIncomeI, TVIncome = "" , "", "", ""
def login():
    f2 = Frame(bg="light blue")
    f2.place(x=0, y=0, width=650, height=400)

    g1 = StringVar()
    g2 = StringVar()

    un = Label(f2,text = "Enter Name", bg="light blue", fg= "Black", font=("comicsansms",11))
    un.place(x=200, y=50)
    e1 = Entry(f2, font=("comicsansms",11), textvariable = g1)
    e1.place(x=330, y=50, width = 120)

    up = Label(f2, text="Enter Password", bg="light blue", fg="Black", font=("comicsansms", 11))
    up.place(x=200, y=100)
    e2 = Entry(f2, font=("comicsansms", 11), show="*", textvariable = g2)
    e2.place(x=330, y=100, width=120)

    def login1():
        global data1, data2
        conn = sqlite3.connect("expensetracker.db")
        c = conn.cursor()
        r = c.execute("SELECT * FROM register WHERE uname='"+g1.get()+"' AND upass ='"+g2.get()+"'")
        for r1 in r:
            mymenu()
            displayexpense()
            displayincome()
            messagebox.showinfo("Logged In", "Welcome")
            break
        else:
            messagebox.showinfo("Error Logging", "Invalid or used Username/Password")
        conn.commit()
        conn.close()

        g1.set("")
        g2.set("")



    b1 = Button(f2, text="LogIn",font=("comicsansms", 11), command = login1)
    b1.place(x=300, y=140, width=80,height = 40)

    b2 = Button(f2, text="Home", font=("comicsansms", 11), command = home)
    b2.place(x=20, y=300, width=80, height=40)

    b3 = Button(f2, text="Register", font=("comicsansms",11),command = register)
    b3.place(x=500, y=300, width=80, height=40)

def AddExpense(a=0,d=0,b=0):
    global EDateE, ETitleE, EExpenseE, TVExpense, data1
    a = EDateE.get()
    b = ETitleE.get()
    d = EExpenseE.get()
    data1 = [a,b,d]
    TVExpense.insert("","end",values =data1)
    EDateE.delete(0,END)
    ETitleE.delete(0,END)
    EExpenseE.delete(0,END)

    add_expense(a,b,d)


def AddIncome(e=0, f=0, g=0):

    global EDateI, ETitleI, EIncomeI, TVIncome, data2
    e = EDateI.get()
    f = ETitleI.get()
    g = EIncomeI.get()
    data2 = [e, f, g]
    TVIncome.insert("", "end", values=data2)
    EDateI.delete(0,END)
    ETitleI.delete(0,END)
    EIncomeI.delete(0,END)

    add_income(e,f,g)


def add_expense(a,b,d):
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" INSERT INTO expense VALUES (?,?,?)",(a,b,d))

    conn.commit()
    conn.close()

def add_income(e,f,g):
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" INSERT INTO income VALUES (?,?,?)",(e,f,g))

    conn.commit()
    conn.close()

def displayexpense():
    global data1
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" SELECT * FROM expense ")
    TVList = c.fetchall()
    for i in TVList:

        TVExpense.insert("", "end", values=i)


def displayincome():
    global data2
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" SELECT * FROM income ")
    TVList = c.fetchall()
    for j in TVList:

        TVIncome.insert("", "end", values=j)



def mymenu():
    n = ttk.Notebook()
    n.place(x=0,y=0, width =600, height =400)
    insertdata(n)

def insertdata(n):

    F4 = Frame(n, bg ="light blue")
    F5 = Frame(n, bg ="light blue")
    F6 = Frame(n, bg ="light blue")

    n.add(F4, text="Expense")
    n.add(F5, text="Income")
    n.add(F6, text="Stats")


    global EDateE,ETitleE, EExpenseE, TVExpense
    # Tab 1 - Expense
    LDateE = ttk.Label(F4, text="Date:", font="comicsansms 18")
    LDateE.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    EDateE = DateEntry(F4, width=19, background="blue", foreground="white", font="comicsansms 18")
    EDateE.grid(row=0, column=1, padx=5, pady=5)

    LTitleE = ttk.Label(F4, text="Title:", font="comicsansms 18")
    LTitleE.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    TitleE = StringVar()
    ETitleE = ttk.Entry(F4, textvariable=TitleE, font="comicsansms 18")
    ETitleE.grid(row=1, column=1, padx=5, pady=5)

    LExpenseE = ttk.Label(F4, text="Expense:", font="comicsansms 18")
    LExpenseE.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    ExpenseE = StringVar()
    EExpenseE = ttk.Entry(F4, textvariable=ExpenseE, font="comicsansms 18")
    EExpenseE.grid(row=2, column=1, padx=5, pady=5)

    BF1Add = Button(F4, text="Add", command=AddExpense)
    BF1Add.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    # Tree View for Expense
    TVList = ["Date", "Title", "Expense"]

    TVExpense = ttk.Treeview(F4, column=TVList, show="headings", height=5)
    for i in TVList:
        TVExpense.heading(i, text=i.title())

    TVExpense.grid(row=5, column=0, padx=5, pady=5, sticky="w", columnspan=3)

    # Tab2 Income
    global EDateI, ETitleI, EIncomeI, TVIncome
    LDateI = ttk.Label(F5, text="Date:", font="comicsansms 18")
    LDateI.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    EDateI = DateEntry(F5, width=19, background="blue", foreground="white", font="comicsansms 18")
    EDateI.grid(row=0, column=1, padx=5, pady=5)

    LTitleI = ttk.Label(F5, text="Title:", font="comicsansms 18")
    LTitleI.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    TitleI = StringVar()
    ETitleI = ttk.Entry(F5, textvariable=TitleI, font="comicsansms 18")
    ETitleI.grid(row=1, column=1, padx=5, pady=5)

    LIncomeI = ttk.Label(F5, text="Expense:", font="comicsansms 18")
    LIncomeI.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    IncomeI = StringVar()
    EIncomeI = ttk.Entry(F5, textvariable=IncomeI, font="comicsansms 18")
    EIncomeI.grid(row=2, column=1, padx=5, pady=5)

    BF2Add = Button(F5, text="Add", command=AddIncome)
    BF2Add.grid(row=4, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    # Tree View for Expense
    TVList = ["Date", "Title", "Income"]
    TVIncome = ttk.Treeview(F5, column=TVList, show="headings", height=5)
    for i in TVList:
        TVIncome.heading(i, text=i.title())
    TVIncome.grid(row=5, column=0, padx=5, pady=5, sticky="w", columnspan=3)


def register():
    f3 = Frame(bg="light blue")
    f3.place(x=0, y=0, width=650, height=400)

    r1 = StringVar()
    r2 = StringVar()
    r3 = StringVar()


    un = Label(f3,text = "Enter Name", bg="light blue", fg= "Black", font=("comicsansms",11))
    un.place(x=200, y=50)
    e1 = Entry(f3, font=("comicsansms",11), textvariable= r1)
    e1.place(x=330, y=50, width = 120)

    up = Label(f3, text="Enter Password", bg="light blue", fg="Black", font=("comicsansms", 11))
    up.place(x=200, y=100)
    e2 = Entry(f3, font=("comicsansms", 11), show="*", textvariable= r2)
    e2.place(x=330, y=100, width=120)

    up = Label(f3, text="Enter C.Number", bg="light blue", fg="Black", font=("comicsansms", 11))
    up.place(x=200, y=150)
    e2 = Entry(f3, font=("comicsansms", 11), textvariable= r3)
    e2.place(x=330, y=150, width=120)

    def regis1():
        conn = sqlite3.connect("expensetracker.db")
        c = conn.cursor()
        c.execute("INSERT INTO register VALUES ('"+r1.get()+"', '"+r2.get()+"', '"+r3.get()+"')")
        print("data inserted")
        conn.commit()
        conn.close()
        messagebox.showinfo("Registration", "Registered Sucessfully, please login now")
        r1.set("")
        r2.set("")
        r3.set("")



    b1 = Button(f3, text="Register",font=("comicsansms", 11), command = regis1)
    b1.place(x=300, y=180, width=80,height = 40)

    b2 = Button(f3, text="Home", font=("comicsansms", 11), command = home)
    b2.place(x=20, y=300, width=80, height=40)

    b3 = Button(f3, text="LogIn", font=("comicsansms", 11), command= login)
    b3.place(x=500, y=300, width=80, height=40)


def home():
    f1 = Frame(bg="light blue")
    f1.place(x=0,y=0,width = 650,height =400)
    b1 = Button(f1,text="LogIn",command=login)
    b1.place(x = 220,y=100, width=80,height = 40)
    b2 = Button(f1, text="Register", command= register)
    b2.place(x=320, y=100, width=80, height=40)
home()
root.mainloop()
