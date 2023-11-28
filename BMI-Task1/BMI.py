from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

box = Tk()
box.title("BMI CALCULATOR")
box.geometry("450x580+300+200")
box.resizable(True,True)
box.configure(bg="#f0f1f5")


icon = PhotoImage(file ="icon.png")
box.iconphoto(False,icon)
top = ImageTk.PhotoImage(Image.open("top3.png"))
topimg = Label(box,image = top,background = "#f0f1f5")
topimg.place(x = 75,y =-10)

Label(box,width =72,height =18,bg ="#172c7e").pack(side = BOTTOM)

box1 = PhotoImage(file ="box.png")
Label(box,image = box1).place(x=5,y=90)
Label(box,image = box1).place(x=230,y=90)
Label(box,text="Height",font="Impact 18",bg="white").place(x=70,y=110)
Label(box,text="Weight",font="Impact 18",bg="white").place(x=295,y=110)
scale = PhotoImage(file = "scale.png")
Label(box,image = scale,bg="#172c7e").place(x=5,y=310)
#height slider
curr = tk.DoubleVar()
def get_curr():
    return '{: .2f}'.format(curr.get())
def slider_changed(event):
    Height.set(get_curr())
    size = int(float(get_curr()))
    img = (Image.open("man3.png"))
    resize = img.resize((150,20+size))
    pic2=ImageTk.PhotoImage(resize)
    manimg.config(image=pic2)
    manimg.place(x=70,y=540-size)
    manimg.image = pic2
style =ttk.Style()
style.configure("TScale",background="white")

slider = ttk.Scale(box, from_=0, to=220,orient='horizontal',style ="TScale",command = slider_changed,variable = curr)
slider.place(x=70,y=220)
#weight slider
curr2 = tk.DoubleVar()
def get_curr2():
    return '{: .2f}'.format(curr2.get())
def slider_changed2(event):
    Weight.set(get_curr2())
style2 =ttk.Style()
style2.configure("TScale",background="white")

slider2 = ttk.Scale(box, from_=0, to=220,orient='horizontal',style ="TScale",command = slider_changed2,variable = curr2)
slider2.place(x=290,y=220)
#height
Height = StringVar()
height = Entry(box,textvariable=Height,width =5, font = 'Impact 30', bg = '#fff', fg = '#000', bd = 0,justify = CENTER)
height.place(x=40,y=160)
Height.set(get_curr())
#weight
Weight = StringVar()
weight = Entry(box,textvariable=Weight,width =5, font = 'Impact 30', bg = '#fff', fg = '#000', bd = 0,justify = CENTER)
weight.place(x=260,y=160)
Weight.set(get_curr2())

manimg = Label(box,bg = "#172c7e")
manimg.place(x=70,y=500)

def BMI():
    h=float(Height.get())
    w=float(Weight.get())
    m=h/100
    bmi=round(float(w/m**2),1)
    Label1.config(text=bmi)

    if bmi<=18.5:
        Label2.config(text="Underweight")
    elif bmi>18.5 and bmi<=25:
        Label2.config(text="Normal")
    elif bmi>25 and bmi<=30:
        Label2.config(text="Overweight")
    else:
        Label2.config(text="Obese")

Button(box,text="View Report", width=15,height=2,font="Roboto 10",bg="#fff",fg="#172c7e",command=BMI).place(x=220,y=340)

Label1=Label(box,font="Brooklyn 25 ",bg="#172c7e",fg="#ffa500")
Label1.place(x=210,y=395)

Label2=Label(box,font="Arial 20 bold",bg="#172c7e",fg="#ffa500")
Label2.place(x=210,y=430)



box.mainloop()