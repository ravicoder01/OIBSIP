from tkinter import *

def bmi():
    BMI=float(weightpass.get())/float(heightpass.get())**2
   
    if BMI<=18:
         result=Label(root,text=f"your BMI is : {BMI} and you are Underweight",font="comicsansms 10 bold",fg="GREEN")
         result.grid(row=4,column=1)
   
    if BMI>18 and BMI<=25:
         result=Label(root,text=f"your BMI is : {BMI} that is absolutely Normal",font="comicsansms 10 bold",fg="GREEN")
         result.grid(row=4,column=1)
        
    if BMI>25:
         result=Label(root,text=f"your BMI is : {BMI} and you are Overweight",font="comicsansms 10 bold",fg="GREEN")
    
         result.grid(row=4,column=1)


root=Tk()
root.geometry("300x300")

lable1=Label(root,text="BMI CALCULATOR",font="comicsansms 10 bold",fg="RED")
lable1.grid(row=0,column=2)

weight=Label(root,text="Enter your weight in kg",font="comicsansms 9 bold").grid(row=1,column=0)
height=Label(root,text="Enter your height in meter",font="comicsansms 9 bold").grid(row=2,column=0)

weightpass=IntVar()
heightpass=IntVar()

w=Entry(root,textvar=weightpass).grid(row=1,column=1)
h=Entry(root,textvar=heightpass).grid(row=2,column=1)

Button(root,text="Click to calculate BMI",command=bmi).grid(row=3,column=1)

root.mainloop()