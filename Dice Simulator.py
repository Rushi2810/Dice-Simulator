from tkinter import *
import random

#For Window,Window Size and its title
screen=Tk()
screen.geometry("350x400")
screen.title("Dice Simulator")

#Images of Dices from 1 To 6
dice1=PhotoImage(file="Dice#1.png")
dice2=PhotoImage(file="Dice#2.png")
dice3=PhotoImage(file="Dice#3.png")
dice4=PhotoImage(file="Dice#4.png")
dice5=PhotoImage(file="Dice#5.png")
dice6=PhotoImage(file="Dice#6.png")

#Creating List
DICE=[dice1,dice2,dice3,dice4,dice5,dice6]


def roll():
    d=random.choice(DICE) #Using Random to choose dice images randomly
    t=Label(screen,image=d) #To show dice image on the window   
    t.place(x=50,y=20) #To place Image place
    
b=Button(screen,text="Roll The Dice", font={"Arial",14},command=roll) #Button to Call def roll using "command"
b.place(x=110,y=310) #Place of Dice
