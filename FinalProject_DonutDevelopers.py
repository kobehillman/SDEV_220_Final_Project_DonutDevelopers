# Author(s): The Donut Developers (Kobe, Yailyn, Alic)
# Date Written:
# FinalProject_DonutDevelopers

import tkinter
# Import the required Libraries
from tkinter import *
from tkinter import ttk

welcomeWindow = Tk()

welcomeWindow.geometry("750x250")
# welcomeWindow.title = ('Wecome to Mary Lou Donuts!')
# Create Button(s)
Label(welcomeWindow, text="Welcome to Mary Lou Donuts! Please choose from the following options!").pack(pady=20)
welcomeWindow.geometry("750x250")

Button(welcomeWindow, text=("About Us"), width = 20,
        # command = aboutUsNo next window set up
        ).pack(pady=0)
Button(welcomeWindow, text=("Place Order"), width = 20,
        # command = oder No next window set up
       ).pack(pady=0)
Button(welcomeWindow, text=("Menu"), width = 20,
       command = Menu
       ).pack(pady=0)

def Menu():
    Menu = tkinter.Toplevel()
    Menu.geometry("750x250")
    Menu.title = ('Wecome to Mary Lou Donuts!')
# Create Button(s)
    Label(Menu, text = "Here's our collection of Donuts!").pack(pady=20)
    Button(Menu, text = ("Donut 1"), width = 20).pack(pady=15)
    Button(Menu, text = ("Donut 2"), width = 20).pack(pady=15)
    Button(Menu, text = ("Donut 3"), width = 20).pack(pady=15)
    Button(Menu, text = ("Donut 4"), width = 20).pack(pady=15)
    Button(Menu, text = ("Donut 5"), width = 20).pack(pady=15)

welcomeWindow.mainloop()