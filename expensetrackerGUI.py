from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar import DateEntry
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import matplotlib.pyplot as plt


root=Tk()
root.title("Expense Tracker")
root.geometry("600x400")
root.resizable(0,0)
#root.config(bg="black")
EDateE, ETitleE, EExpenseE, TVExpense = "" , "", "", ""

EDateI, ETitleI, EIncomeI, TVIncome = "" , "", "", ""

F6 = ""

def login():
    global g1
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
        r = c.execute("SELECT * FROM register WHERE name='"+g1.get()+"' AND pass ='"+g2.get()+"'")
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
        global username
        username = g1.get()
        #g1.set("")
        #g2.set("")



    b1 = Button(f2, text="LogIn",font=("comicsansms", 11), command = login1)
    b1.place(x=300, y=140, width=80,height = 40)

    b2 = Button(f2, text="Home", font=("comicsansms", 11), command = home)
    b2.place(x=20, y=300, width=80, height=40)

    b3 = Button(f2, text="Register", font=("comicsansms",11),command = register)
    b3.place(x=500, y=300, width=80, height=40)

def AddExpense(a=0,d=0,b=0):
    global EDateE, ETitleE, EExpenseE, TVExpense, data1, exp_fk
    exp_fk = g1.get()
    a = EDateE.get()
    b = ETitleE.get()
    d = EExpenseE.get()
    data1 = [a,b,d]
    TVExpense.insert("","end",values =data1)
    EDateE.delete(0,END)
    ETitleE.delete(0,END)
    EExpenseE.delete(0,END)

    add_expense(exp_fk,a,b,d)


def AddIncome(e=0, f=0, g=0):

    global EDateI, ETitleI, EIncomeI, TVIncome, data2, inc_fk
    inc_fk = g1.get()
    e = EDateI.get()
    f = ETitleI.get()
    g = EIncomeI.get()
    data2 = [e, f, g]
    TVIncome.insert("", "end", values=data2)
    EDateI.delete(0,END)
    ETitleI.delete(0,END)
    EIncomeI.delete(0,END)

    add_income(inc_fk,e,f,g)


def add_expense(exp_fk,a,b,d):
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" INSERT INTO expences VALUES (?,?,?,?)",(exp_fk,a,b,d))

    conn.commit()
    conn.close()

def add_income(inc_fk,e,f,g):
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(" INSERT INTO incomes VALUES (?,?,?,?)",(inc_fk,e,f,g))

    conn.commit()
    conn.close()

def displayexpense():
    global data1,exp_fkk
    exp_fkk = g1.get()
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    #c.execute(" SELECT * FROM expences ")
    c.execute(f" SELECT exp_date,exp_title, expense FROM expences WHERE name_exp_fk='{exp_fkk}'")
    TVList = c.fetchall()
    for i in TVList:

        TVExpense.insert("", "end", values=i)


def displayincome():
    global data2, inc_fkk
    inc_fkk = g1.get()
    conn = sqlite3.connect("expensetracker.db")
    c = conn.cursor()
    c.execute(f" SELECT inc_date,inc_title, income FROM incomes WHERE name_inc_fk='{inc_fkk}'")
    TVList = c.fetchall()
    for j in TVList:

        TVIncome.insert("", "end", values=j)



def mymenu():
    n = ttk.Notebook()
    n.place(x=0,y=0, width =600, height =400)
    insertdata(n)

def insertdata(n):
    global F6
    F4 = Frame(n, bg ="light blue")
    F5 = Frame(n, bg ="light blue")
    F6 = Frame(n, bg ="light blue")
    F7 = Frame(n, bg ="light blue")

    n.add(F4, text="Expense")
    n.add(F5, text="Income")
    n.add(F6, text="Expense Stats")
    n.add(F7, text="Income Stats")

# Label frame for stats
#     labelframe = LabelFrame(F6, text=f"Statistics of month")
#     labelframe.pack(fill="both", expand="yes")
#     plot('yeman', 'may', labelframe)
    # Dropdown months for stats
    chvar = StringVar()
    chvar.set("jan")
    months = {"jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"}
    dropdown = OptionMenu(F6, chvar, *months)
    dropdown.grid(row = 1, column = 1)
    global lableframe
    lableframe = LabelFrame(F6, text="Statistics :-")
    lableframe.grid(row =2, column= 1)
    def change_dropdown(*args):
        choice = chvar.get()
        print(choice)
        global username, lableframe
        plot(username, choice, lableframe)

    chvar.trace('w', change_dropdown)



#destroying plot after displaying one to avoid overwriting
    def _clear():
        global choice, fig
        plt.clf()






    destroBtn = Button(F6,text="clear plot",command=_clear)
    destroBtn.place(x=450, y=0)

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

    logout = Button(F4, text="Log Out", command=login)
    logout.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)

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

    logout = Button(F5, text="Log Out", command=login)
    logout.grid(row=8, column=1, padx=5, pady=5, ipadx=5, ipady=5)

    # Tree View for Expense
    TVList = ["Date", "Title", "Income"]
    TVIncome = ttk.Treeview(F5, column=TVList, show="headings", height=5)
    for i in TVList:
        TVIncome.heading(i, text=i.title())
    TVIncome.grid(row=5, column=0, padx=5, pady=5, sticky="w", columnspan=3)



    # tab 3 - Stats



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
        messagebox.showinfo("Registration","Registered Sucessfully, please login now")
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

# statistics part
def plot(name, month, root):
    conn = sqlite3.connect("expensetracker.db")
    curr = conn.cursor()
    curr.execute(f"select * from expences where name_exp_fk= '{name}'")
    data = curr.fetchall()
    #print(data)
    month_dict = {1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "may", 6: "jun", 7: "jul", 8: "aug", 9: "sep", 10: "oct",
                  11: "nov", 12: "dec"}
    dates = [row[1] for row in data]
    expenses = [row[3] for row in data]
    new_dates = []
    new_expenses = []

    for date, expense in zip(dates, expenses):
        if month_dict[int(date[0])] == month:
            new_dates.append(date)
            new_expenses.append(expense)

    # the figure that will contain the plot
    global fig
    fig = plt.Figure(figsize=(6, 3), dpi=100)
    plot1 = fig.add_subplot(111)
    # plotting the graph
    plot1.bar(new_dates, new_expenses)
    global canvas
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().pack()


root.mainloop()
