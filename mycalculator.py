from tkinter import *
import sqlite3
root=Tk()
root.geometry("350x590")
root.resizable(0,0)
root.title("CALCULATOR")
root.config(bg="black")

# Declaring Variable for Screen unit.
screen_var = StringVar()
screen_var.set("")

# Creating space for entering input
screen = Entry(root,textvar=screen_var,font="comicsansms 40")
screen.pack(fill=X,padx=10,pady=10)

# Frame to store all widgets(Buttons)
frames = Frame(root,bg="black",relief=SUNKEN)
frames.pack()

# Creating function for clicking button
def click(event):
    global screen_var
    text = event.widget.cget("text")
    try:
        if text=='C':
            screen_var.set('')
        elif text=='<-X':
            screen_var.set(screen_var.get()[0:-1])
        elif text == '=':
            if screen_var.get().isdigit():
                pass
            else:
                screen_var.set(eval(screen_var.get()))
        elif text=='+/-':
            if screen_var.get().isdigit():
                screen_var.set('-'+screen_var.get())
        else:
            un_supported=['+','-','*','/','%','.',')','**']
            if text in un_supported:
                if screen_var.get()=='' or (screen_var.get()[-1] in un_supported):
                    pass
                else:
                    screen_var.set(screen_var.get()+ text)
            else:
                screen_var.set(screen_var.get()+ text)
    except:
        screen_var.set(f'Wrong input ({screen_var.get()})')
    screen.update()

# List pf buttons to be added in calculator
lists=['C','<-X','%','/','(',')','**','+/-',9,8,7,'*',6,5,4,'-',3,2,1,'+',0,'00','.','=']
count=0

#For inserting buttons in respective manner
for r in range(6):
    for c in range(4):
        b=Button(frames,width=3,height=1,text=str(lists[count]),font=("lucida 30"),bg="lightyellow")
        b.grid(row=r,column=c,padx=2,pady=2)
        b.bind("<Button-1>",click)
        count+=1



root.mainloop()
