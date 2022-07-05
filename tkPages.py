# Import Base Libs
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

"""
Make a class for every new page you want to create, this is to better organize your TK pages.
In the class make a function called create which contains widgets(Labels, Images, TextFeilds)
that you want to on that page.
When making widgets ensure to always use 'self.' before the naming the var.
Always use grid, not pack or place
"""
########################## - Program - ##########################


class loginpage():  # login page class
    def create(self):  # Function will create widgets when invoked
        # Get the photo from computer
        self.photo = tk.PhotoImage(file='./img/logo.png')

        # Make a label using the image we got
        self.image_label = ttk.Label(self, image=self.photo,)
        self.image_label.grid(row=1, column=1)  # Place 1st row

        # Create a Frame for login widgets
        self.loginentrys = ttk.Frame(self)  # Frame
        self.loginentrys.grid(row=2, column=1, sticky="nsew", rowspan=2)
        # Setup columns
        self.loginentrys.columnconfigure(index=0, weight=1)
        self.loginentrys.columnconfigure(index=1, weight=1)

        # Email Entry ---
        self.emalimg = tk.PhotoImage(file='./img/email.png')  # Get email icon
        # Create icon in nested 1st column and email entry in 2nd
        self.emalicon = ttk.Label(self.loginentrys, image=self.emalimg)
        self.emalicon.grid(row=0, column=0, sticky="ne", pady=10)
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
        self.loginBtn = ttk.Button(
            self,
            text="Login",
            style="big.TButton",
            command=lambda: self.login(self.email.get(), self.pswd.get()))  # ChangePage 1, meaning it will open index 1 of pages list
        self.loginBtn.grid(row=4, column=1, pady=10)  # Place 4th row

        # Signup button
        self.signupBtn = ttk.Button(
            self,
            text="Signup",
            style="small.TButton",
            command=lambda: self.changePage(1))  # ChangePage 1, meaning it will open index 1 of pages list
        self.signupBtn.grid(row=5, column=1, pady=10)  # Place 4th row


class signpage():  # signup page page class
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

        # Name Entry ---
        self.nameimg = tk.PhotoImage(file='./img/user.png')  # Get name icon
        # Create icon in nested 1st column and name entry in 2nd
        self.nameicon = ttk.Label(self.loginentrys, image=self.nameimg)
        self.nameicon.grid(row=0, column=0, sticky="ne", pady=10)
        self.name = ttk.Entry(self.loginentrys)
        self.name.grid(row=0, column=1, pady=10)

        # Email Entry ---
        self.emalimg = tk.PhotoImage(file='./img/email.png')  # Get email icon
        # Create icon in nested 1st column and email entry in 2nd
        self.emalicon = ttk.Label(self.loginentrys, image=self.emalimg)
        self.emalicon.grid(row=1, column=0, sticky="ne", pady=10)
        self.email = ttk.Entry(self.loginentrys)
        self.email.grid(row=1, column=1, pady=10)

        # Password Entry ---
        self.pswdimg = tk.PhotoImage(file='./img/pswd.png')  # Get pswd icon
        # Create icon in nested 1st column and password entry in 2nd but 2nd row
        self.pswdicon = ttk.Label(self.loginentrys, image=self.pswdimg)
        self.pswdicon.grid(row=2, column=0, sticky="ne", pady=10)
        self.pswd = ttk.Entry(self.loginentrys)
        self.pswd.grid(row=2, column=1, pady=10)

        # Confirm Password Entry ---
        self.conPswdicon = ttk.Label(self.loginentrys, image=self.pswdimg)
        self.conPswdicon.grid(row=3, column=0, sticky="ne", pady=10)
        self.conPswd = ttk.Entry(self.loginentrys)
        self.conPswd.grid(row=3, column=1, pady=10)

        # Create a button that will call the changePage call (in the main file)
        self.signupBtn = ttk.Button(
            self,
            text="Signup",
            command=lambda: self.signup(self.name.get(), self.email.get(), self.pswd.get(), self.conPswd.get()))  # ChangePage 1, meaning it will open index 1 of pages list
        self.signupBtn.grid(row=4, column=1, pady=10)  # Place 4th row
        # Signup button
        self.loginBtn = ttk.Button(
            self,
            text="Login",
            style="small.TButton",
            command=lambda: self.changePage(0))  # ChangePage 1, meaning it will open index 1 of pages list
        self.loginBtn.grid(row=5, column=1, pady=10)  # Place 4th row


class mainpage():  # main page class
    def create(self):
        # Create graph before creating other widgets
        self.graphInit()
        # Get the photo from computer
        self.image = Image.open('./img/graph.png')
        # Resize from 640 × 480 to 480 x 360
        self.image = self.image.resize((480, 360), Image.ANTIALIAS)
        # Convert resized img to PhotoImage
        self.photo = ImageTk.PhotoImage(self.image)
        # Make a label using the image we got
        self.image_label = ttk.Label(self, image=self.photo,)
        self.image_label.grid(row=1, column=1)  # Place 1st row
        # Welcome label
        self.welcomelabel = ttk.Label(
            self,
            text="Login successful!\nWelcome to the main page!",
            font=("Arial", 25)
        )
        # Place label
        self.welcomelabel.grid(
            row=2,
            column=1,
            pady=10)
        # Create a Frame for bunch of buttons sideways
        self.multibtn = ttk.Frame(self)  # Frame
        self.multibtn.grid(row=3, column=1, pady=20)
        # Setup columns
        for i in range(2):
            self.multibtn.columnconfigure(index=i, weight=1)
        # Create button for weight form in multibtn frame
        self.weightBtn = ttk.Button(
            self.multibtn,
            text="Weight",
            command=lambda: self.changePage(3))
        # Place it on first from left
        self.weightBtn.grid(
            row=0,
            column=0,
            padx=10)
        # Create button for food form in multibtn frame
        self.foodBtn = ttk.Button(
            self.multibtn,
            text="Food",
            command=lambda: self.changePage(4))
        # Place it on second from left
        self.foodBtn.grid(
            row=0,
            column=1,
            padx=10)
        # Create button to logout and goto login page
        self.logoutBtn = ttk.Button(
            self.multibtn,
            text="Logout",
            command=lambda: self.changePage(0))
        # Place it on thrid from left
        self.logoutBtn.grid(
            row=0,
            column=2,
            padx=10)


class weightForm():  # page that lets user enter weight to DB
    def create(self):
        # Create a Frame for login widgets
        self.entries = ttk.Frame(self)  # Frame
        self.entries.grid(row=2, column=1, sticky="nsew", rowspan=2)
        # Setup columns
        self.entries.columnconfigure(index=0, weight=1)
        self.entries.columnconfigure(index=1, weight=1)

        # Weight Entry ---
        self.weightimg = tk.PhotoImage(file='./img/weight.png')  # pswd icon
        self.weighticon = ttk.Label(self.entries, image=self.weightimg)
        self.weighticon.grid(row=3, column=0, sticky="ne", pady=10)
        self.weight = ttk.Entry(self.entries)
        self.weight.grid(row=3, column=1, pady=10)

        # Create a button that will call the changePage call (in the main file)
        self.sumbitBtn = ttk.Button(
            self,
            text="Enter",
            command=lambda: self.weightForm(self.weight.get()))
        self.sumbitBtn.grid(row=4, column=1, pady=10)  # Place 4th row


class foodForm():  # page that lets the user enter food nutr to DB
    def create(self):
        self.prevEntry = ""
        # Create a Frame for login widgets
        self.entries = ttk.Frame(self)  # Frame
        self.entries.grid(row=2, column=1, sticky="nsew",
                          rowspan=2, padx=10, pady=10)
        # Setup columns
        self.entries.columnconfigure(index=0, weight=1)
        self.entries.columnconfigure(index=1, weight=1)

        # Food Entry ---
        self.foodimg = tk.PhotoImage(file='./img/food.png')  # pswd icon
        self.foodicon = ttk.Label(self.entries, image=self.foodimg)
        self.foodicon.grid(row=3, column=0, sticky="ne", pady=10)
        self.food = ttk.Entry(self.entries)
        self.food.grid(row=3, column=1, pady=10, padx=10)

        # Confirm Label
        self.confLblStr = tk.StringVar()
        self.confLbl = ttk.Label(self, textvariable=self.confLblStr)
        self.confLbl.grid(row=4, column=1, pady=2)  # Place 4th row

        # Create a button that will call the changePage call (in the main file)
        self.btnStr = tk.StringVar()
        self.btnStr.set("Enter")
        self.sumbitBtn = ttk.Button(
            self,
            textvariable=self.btnStr,
            command=lambda: self.foodForm(self.food.get().lower()))
        self.sumbitBtn.grid(row=5, column=1, pady=10)  # Place 4th row
