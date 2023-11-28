import customtkinter
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.title("Weather App")
root.geometry("900x470+300+300")
root.resizable(False,False)
#icon
icon = PhotoImage(file="logo.png")
root.iconphoto(False,icon)
#temperature box
img = (Image.open("Rounded Rectangle 1.png"))
resize = img.resize((300, 180))
Round = ImageTk.PhotoImage(resize)
Label(root,image=Round,bg="#242424").place(x=30,y=100)
label1=customtkinter.CTkLabel(master=root,text="Temperature",font=("Impact",15),bg_color="#203243",text_color="white").place(x=40, y=90)
label2=customtkinter.CTkLabel(master=root,text="Humidity",font=("Impact",15),bg_color="#203243",text_color="white").place(x=40, y=120)
label3=customtkinter.CTkLabel(master=root,text="Pressure",font=("Impact",15),bg_color="#203243",text_color="white").place(x=40, y=150)
label4=customtkinter.CTkLabel(master=root,text="Wind Speed",font=("Impact",15),bg_color="#203243",text_color="white").place(x=40, y=180)
#search box
search=PhotoImage(file="Rounded Rectangle 3.png")
Label(root,image=search,bg="#242424").place(x=400,y=100)
cloud1=PhotoImage(file="Layer 7.png")
Label(root,image=cloud1,bg="#203243").place(x=420,y=107)
textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203242",fg="white",border=0)
textfield.place(x=500,y=110)
def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)
    lat_long.config(text=f"{round(location.latitude,4)} °N,{round(location.longitude,4)} °E")
    home=pytz.timezone(result)
    localtime=datetime.now(home)
    curr_time=localtime.strftime("%I:%M %p")
    clock.config(text=curr_time)
    #weather
    #api="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.latitude)+"&units=metric&appid=22234a49dd0fbae49541598d92fc8349"

    json_data = requests.get(api).json()
    print(json_data)
    temp=json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure= json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description=json_data['weather'][0]['description']
    clouds=json_data['clouds']['all']
    feels_like = json_data['main']['feels_like']
    sunrise=json_data['sys']['sunrise']
    dt_obj=datetime.utcfromtimestamp(sunrise)
    time=dt_obj.strftime('%H:%M')
    sunset=json_data['sys']['sunset']
    dt_obj2=datetime.utcfromtimestamp(sunset)
    time2=dt_obj2.strftime('%H:%M')

    t.config(text=(temp,"°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    firstdayimg=json_data['weather'][0]['icon']
    photo1=ImageTk.PhotoImage(file=f"{firstdayimg}@2x.png")
    firstimg.config(image=photo1)
    firstimg.image=photo1


    first_day=datetime.now(home)
    day1.config(text=first_day.strftime("%A"))
    data_label2.config(text=description)
    data_label3.config(text=(clouds,"%"))
    data_label4.config(text=(feels_like,"°C"))
    data_label5.config(text=("Sunrise:",time))
    data_label6.config(text=("Sunset:", time2))


#icon

search_icon=PhotoImage(file="Layer 6.png")
button1=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather).place(x=780,y=104)


#Frame
frame=Frame(root,width=1200,height=200,bg="#203243").pack(side=BOTTOM)
box1=PhotoImage(file="Rounded Rectangle 2.png")
Label(frame,image=box1,bg="#84e4f7").place(x=30,y=420)
box2=PhotoImage(file="Rounded Rectangle 2.png")
Label(frame,image=box2,bg="#84e4f7").place(x=300,y=420)
Label(frame,image=box2,bg="#84e4f7").place(x=570,y=420)
Label(frame,image=box2,bg="#84e4f7").place(x=840,y=420)


#clock
clock=Label(root,font=("Roboto" ,30,'bold'),bg="#242424",fg="white")
clock.place(x=30,y=30)
timezone=Label(root,font=("Roboto",20,'bold'),bg="#242424",fg="white")
timezone.place(x=850,y=30)
lat_long=Label(root,font=("Roboto",10,'bold'),bg="#242424",fg="white")
lat_long.place(x=850,y=60)

#temperature box contents
t=Label(root,font=("Helvetica",15),bg="#203243",fg="white")
t.place(x=200,y=115)
h=Label(root,font=("Helvetica",15),bg="#203243",fg="white")
h.place(x=200,y=150)
p=Label(root,font=("Helvetica",15),bg="#203243",fg="white")
p.place(x=200,y=187)
w=Label(root,font=("Helvetica",15),bg="#203243",fg="white")
w.place(x=200,y=225)

#weekly weather cells

first=Frame(root,width=230,height=132,bg="#282829")
first.place(x=35,y=425)

day1=Label(first,font="arial 20",bg="#282829",fg="#fff")
day1.place(x=90,y=5)
data_label5=Label(first,font="arial 13",bg="#282829",fg="#84e4f7")
data_label5.place(x=110,y=50)
data_label6=Label(first,font="arial 13",bg="#282829",fg="#84e4f7")
data_label6.place(x=110,y=70)

firstimg=Label(first,bg="#282829")
firstimg.place(x=1,y=40)

second=Frame(root,width=150,height=115,bg="#282829")
second.place(x=355,y=435)

day2=Label(second,font="arial 14 bold",text="Description",bg="#282829",fg="#fff")
day2.place(x=5,y=2)
data_label2=Label(second,font="arial 15",bg="#282829",fg="#fff")
data_label2.place(x=5,y=40)


third=Frame(root,width=150,height=115,bg="#282829")
third.place(x=630,y=435)

day3=Label(third,font="arial 14 bold",text="Clouds",bg="#282829",fg="#fff")
day3.place(x=13,y=2)
data_label3=Label(third,font="arial 20",bg="#282829",fg="#fff")
data_label3.place(x=13,y=40)


fourth=Frame(root,width=150,height=115,bg="#282829")
fourth.place(x=890,y=435)

day4=Label(fourth,font="arial 15 bold",text="Feels-like",bg="#282829",fg="#fff")
day4.place(x=18,y=2)
data_label4=Label(fourth,font="arial 20",bg="#282829",fg="#fff")
data_label4.place(x=18,y=40)

root.mainloop()