# Import Base Libs
import tkinter as tk
from tkinter import ttk

# Temp libs
import random


"""
Make a class for every new page you want to create, this is to better organize your TK pages.
In the class make a function called create which contains widgets(Labels, Images, TextFeilds)
that you want to on that page.
When making widgets ensure to always use 'self.' before the naming the var.
Always use grid, not pack or place
"""
########################## - Program - ##########################


class loginpage():  # Home page class
    def create(self):  # Function will create widgets when invoked
        # Get the photo from computer
        self.photo = tk.PhotoImage(file='./img/logo.png')

        # Make a label using the image we got
        self.image_label = ttk.Label(self, image=self.photo)
        self.image_label.grid(row=1, column=1)  # Place 1st row

        # Create a Frame for login widgets
        self.loginentrys = ttk.Frame(self)  # Frame
        self.loginentrys.grid(row=2, column=1, sticky="nsew", rowspan=2)
        # Setup columns
        self.loginentrys.columnconfigure(index=0, weight=1)
        self.loginentrys.columnconfigure(index=1, weight=1)

        # Username Entry ---
        self.userimg = tk.PhotoImage(file='./img/user.png')  # Get user icon
        # Create icon in nested 1st column and username entry in 2nd
        self.usericon = ttk.Label(self.loginentrys, image=self.userimg)
        self.usericon.grid(row=0, column=0, sticky="ne", pady=10)
        self.email = ttk.Entry(self.loginentrys)
        self.email.grid(row=0, column=1, pady=10)

        # Password Entry ---
        self.pswdimg = tk.PhotoImage(file='./img/pswd.png')  # Get pswd icon
        # Create icon in nested 1st column and password entry in 2nd but 2nd row
        self.pswdicon = ttk.Label(self.loginentrys, image=self.pswdimg)
        self.pswdicon.grid(row=1, column=0, sticky="ne", pady=10)
        self.pswd = ttk.Entry(self.loginentrys)
        self.pswd.grid(row=1, column=1, pady=10)

        # Create a button that will call the changePage call (in the main file)
        self.button = ttk.Button(
            self,
            text="Login",
            command=lambda: self.login(self.email.get(), self.pswd.get()))  # ChangePage 1, meaning it will open index 1 of pages list
        self.button.grid(row=4, column=1, pady=10)  # Place 4th row


# no comments u get the idea
class testpage():
    def create(self):
        lines = open('quotes.txt').read().splitlines()
        self.randQuote = random.choice(lines)
        self.label = ttk.Label(
            self,
            text=self.randQuote,
            font=("Arial", 25)
        )
        self.label.grid(
            row=1,
            column=1,
            pady=10)
        self.button = ttk.Button(
            self,
            text="Prev Page",
            command=lambda: self.changePage(0))  # Note that I used 0 because the homepage is the 0th index in list
        self.button.grid(
            row=2,
            column=1,
            pady=10)
