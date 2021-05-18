from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.geometry("320x500")
root.resizable(0,0)
root.config(bg="black")

conn = sqlite3.connect("GymData.db")
c = conn.cursor()
#c.execute()
conn.commit()
conn.close()

def getvalues():
    tmsg.showinfo("Submitted",f"Thank you for your interest {namevalue.get()}, we will get back to you shortly!!")
    nameentry.delete(0,END)
    ageentry.delete(0,END)
    dobvalue.delete(0,END)
    heightentry.delete(0,END)
    weightentry.delete(0,END)




# Read the Image
image = Image.open("dumbellnew.png")

# Reszie the image using resize() method
resize_image = image.resize((200, 100))

img = ImageTk.PhotoImage(resize_image)


Label(text="Welcome to MyGYM",font="comicsansms 10 bold").pack(padx=20,pady=20)

# create label and add resize image
label1 = Label(image=img,bg="yellow")
label1.image = img
label1.pack(side=TOP,fill =X)
f1 = Frame(root,relief=SUNKEN)
f1.pack(padx=20,pady=20,side = TOP)


name = Label(f1,text="Name:",font="comicsansms 13 ")
age = Label(f1,text = "Age:",font="comicsansms 13 ")
dob = Label(f1,text = "DOB:",font="comicsansms 13 ")
height = Label(f1,text = "Height:",font="comicsansms 13 ")
weight = Label(f1,text = "Weight:",font="comicsansms 13 ")

name.grid(row=0)
age.grid(row=1)
dob.grid(row=2)
height.grid(row=3)
weight.grid(row=4)

namevalue = StringVar()
agevalue = IntVar()
dobvalue = IntVar()
heightvalue = IntVar()
weightvalue = IntVar()

nameentry = Entry(f1,textvariable = namevalue,font="comicsansms 13 ")
ageentry = Entry(f1,textvariable= agevalue,font="comicsansms 13 ")
dobvalue = Entry(f1,textvariable= dobvalue,font="comicsansms 13 ")
heightentry = Entry(f1,textvariable = heightvalue,font="comicsansms 13 ")
weightentry = Entry(f1,textvariable = weightvalue,font="comicsansms 13 ")

nameentry.grid(row =0,column =1,padx=5)
ageentry.grid(row =1,column =1,padx=5)
dobvalue.grid(row =2,column =1,padx=5)
heightentry.grid(row =3,column =1,padx=5)
weightentry.grid(row =4,column =1,padx=5)



pt = Checkbutton(f1,text = "Want Personal Trainer",font ="comicsansms 13").grid(row = 5,column =1)
cardio=Checkbutton(f1,text = "Cardio",font ="comicsansms 13").grid(row = 5,column =0)



Button(text = "SUBMIT",command = getvalues).pack(padx=20,fill=X)

root.mainloop()
