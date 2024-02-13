# Author(s): The Donut Developers (Kobe, Yailyn, Alic)
# Date Written:
# FinalProject_DonutDevelopers

import tkinter
# Import the required Libraries
from tkinter import *
from tkinter import ttk

welcomeWindow = Tk()

def Menu():
    Menu = tkinter.Toplevel()
    Menu.geometry("750x250")
    Menu.title = ('Wecome to Mary Lou Donuts!')
    # Create Button(s)
    Label(Menu, text="Here's our collection of Donuts!").pack(pady=20)
    Button(Menu, text=("Donut 1"), width=20).pack(pady=15)
    Button(Menu, text=("Donut 2"), width=20).pack(pady=15)
    Button(Menu, text=("Donut 3"), width=20).pack(pady=15)
    Button(Menu, text=("Donut 4"), width=20).pack(pady=15)
    Button(Menu, text=("Donut 5"), width=20).pack(pady=15)

def aboutUs():
    aboutUs = tkinter.Toplevel()
    aboutUs.geometry("750x250")
    aboutUs.title = ('Wecome to Mary Lou Donuts!')
    # Create Label & Button(s)
    Label(aboutUs, text="This is out History! \n This is what we do! \n This is some other third thing!").pack(pady=20)

def placeOrder():
    placeOrder = tkinter.Toplevel()
    placeOrder.geometry("750x300")
    placeOrder.title = ('Text')
    # Create Label & Button(s)
    Label(placeOrder, text="Place your order here!"
                          "\nWe need to figure out a way to increment a variable everytime someone presses a buton"
                          "\nThat way we can tell how many of something someone orders, instead only being able to order 1"
                          "\nThis could be done with A LOT of windows, but it would be messy and hard to read"
                          "\nBTW the 'Finish Order' Button just closes everything until we have confirmation window").pack(pady=20)
    Button(placeOrder, text=("Placeholder Item1"), width=20).pack(pady=10)
    Button(placeOrder, text=("Placeholder Item2"), width=20).pack(pady=10)
    Button(placeOrder, text=("Placeholder Item3"), width=20).pack(pady=10)
    Button(placeOrder, text=("Finish Order"), width=20, command = welcomeWindow.destroy).pack(pady=1)

welcomeWindow.geometry("750x250")
# welcomeWindow.title = ('Welcome to Mary Lou Donuts!')
# Create Button(s)
Label(welcomeWindow, text="Welcome to Mary Lou Donuts! Please choose from the following options.").pack(pady=20)
welcomeWindow.geometry("750x250")

Button(welcomeWindow, text=("About Us"), width=20,command = aboutUs).pack(pady=0)
Button(welcomeWindow, text=("Place Order"), width=20, command = placeOrder).pack(pady=0)
Button(welcomeWindow, text=("Menu"), width=20, command=Menu).pack(pady=0)
Button(welcomeWindow, text="Leave", width=20, command = welcomeWindow.destroy).pack(pady=0)

welcomeWindow.mainloop()

# DO NOT DELETE - BELOW IS THE BASE SETUP FOR ANY WINDOW
# Replace all '?'s with the variable you want set up for the window
# Make sure that the '!' matches the command listed in the button that goes to this window
#def !():
#   ? = tkinter.Toplevel()
#   ?.geometry("750x250")
#   ?.title = ('Text')
    # Create Label & Button(s)
#   Label(?, text="Text").pack(pady=20)
#   Button(?, text=("Text"), width=20).pack(pady=15)
