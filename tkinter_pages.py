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

        # Frame for small btns
        self.smallbtns = ttk.Frame(self)  # Frame
        self.smallbtns.grid(row=5,column=1, pady=10) 
        # Signup button
        self.signupBtn = ttk.Button(
            self.smallbtns,
            text="Signup",
            style="small.TButton",
            command=lambda: self.changePage(1))  # ChangePage 1, meaning it will open index 1 of pages list
        self.signupBtn.grid(row=0, column=0, padx=3)  # Place 4th row

        # Quit button
        self.quitBtn = ttk.Button(
            self.smallbtns,
            text="Quit",
            style="small.TButton",
            command=lambda: self.quitapp())
        self.quitBtn.grid(row=0, column=1, padx=3)  # Place 4th row
        # Set focus on email entry
        self.email.focus()  

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
        # Get random qoute of the day for that user
        self.q = self.qouteoftheday()
        # Welcome label
        self.welcomelabel = ttk.Label(
            self,
            text="Welcome back "+ self.name.capitalize() +"!",
            font=("Arial", 25)
        )
        # Place label
        self.welcomelabel.grid(
            row=1,
            column=1,
            pady=10)
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
        self.image_label.grid(row=2, column=1)  # Place 1st row
        # Make a label for the qoute
        self.qoutelbl = ttk.Label(self, text=self.q, font=("Arial", 10),wraplength=400)
        self.qoutelbl.grid(row=3, column=1,pady=3)
        # Create a Frame for bunch of buttons sideways
        self.multibtn = ttk.Frame(self)  # Frame
        self.multibtn.grid(row=4, column=1, pady=20)
        # Setup columns
        for i in range(3):
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
        # Create button for history of food in multibtn frame
        self.historyBtn = ttk.Button(
            self.multibtn,
            text="History",
            command=lambda: self.changePage(5))
        # Place it on third from left
        self.historyBtn.grid(
            row=0,
            column=2,
            padx=10)
        # Create button to logout and goto login page
        self.logoutBtn = ttk.Button(
            self.multibtn,
            text="Logout",
            command=lambda: self.changePage(0))
        # Place it on fourth from left
        self.logoutBtn.grid(
            row=0,
            column=3,
            padx=10)
        
class weightForm():  # page that lets user enter weight to DB
    def create(self):
        # Create a Frame for login widgets
        self.entries = ttk.Frame(self)  # Frame
        self.entries.grid(row=2, column=1, padx=10, pady=20, sticky="nsew", rowspan=2)
        # Setup columns
        self.entries.columnconfigure(index=0, weight=1)
        self.entries.columnconfigure(index=1, weight=1)

        # Weight Entry ---
        self.weightimg = tk.PhotoImage(file='./img/weight.png')  # pswd icon
        self.weighticon = ttk.Label(self.entries, image=self.weightimg)
        self.weighticon.grid(row=3, column=0, sticky="ne", pady=20,padx=10)
        self.weight = ttk.Entry(self.entries)
        self.weight.grid(row=3, column=1, pady=10)

        # Create a button that will call the changePage call (in the main file)
        self.sumbitBtn = ttk.Button(
            self,
            text="Enter",
            style="big.TButton",
            command=lambda: self.weightForm(self.weight.get()))
        self.sumbitBtn.grid(row=4, column=1, pady=10)  # Place 4th row

        # Return home btn
        self.homeBtn = ttk.Button(
            self,
            text="Home",
            style="small.TButton",
            command=lambda: self.changePage(2))
        self.homeBtn.grid(row=5, column=1, pady=5)  # Place 5th row

class foodForm():  # page that lets the user enter food nutr to DB
    def create(self):
        self.prevEntry = ""
        # Create a Frame for login widgets
        self.entries = ttk.Frame(self)  # Frame
        self.entries.grid(row=1, column=1, sticky="nsew",
                          rowspan=2, padx=10, pady=20)
        # Setup columns
        self.entries.columnconfigure(index=0, weight=1)
        self.entries.columnconfigure(index=1, weight=1)

        # Food Entry ---
        self.foodimg = tk.PhotoImage(file='./img/food.png')  # pswd icon
        self.foodicon = ttk.Label(self.entries, image=self.foodimg)
        self.foodicon.grid(row=2, column=0, sticky="ne", pady=20,padx=10)
        self.food = ttk.Entry(self.entries)
        self.food.grid(row=2, column=1, pady=10)

        # Confirm Label
        self.confLblStr = tk.StringVar()
        self.confLbl = ttk.Label(self, textvariable=self.confLblStr)
        self.confLbl.grid(row=3, column=1, pady=2)  # Place 4th row

        # Create a button that will call the changePage call (in the main file)
        self.btnStr = tk.StringVar()
        self.btnStr.set("Enter")
        self.sumbitBtn = ttk.Button(
            self,
            textvariable=self.btnStr,
            style="big.TButton",
            command=lambda: self.foodForm(self.food.get().lower()))
        self.sumbitBtn.grid(row=4, column=1, pady=5)  # Place 4th row

        # Return home btn
        self.homeBtn = ttk.Button(
            self,
            text="Home",
            style="small.TButton",
            command=lambda: self.changePage(2))
        self.homeBtn.grid(row=5, column=1, pady=5)  # Place 5th row

class foodHistory(): # page that get data for db and displays past food ate
    def create(self):
        # Create label to show which user the data is shown for
        self.usernamelbl = ttk.Label(self, text=self.name+"'s Food History", font=("Arial", 25))
        self.usernamelbl.pack()

        # Create frame that will make a border and contain the table for showing data
        self.treeviewframe = ttk.Frame(self)
        self.treeviewframe.pack(pady=20,padx=20)

        # Create a treeview to show data in
        self.foodtable = ttk.Treeview(self.treeviewframe)

        # Create columns for the table
        self.foodtable['columns'] = ('user_food', 'user_cals', 'user_prot', 'user_size')

        # Setup columns for the data
        self.foodtable.column("#0", width=0)
        self.foodtable.column("user_food",anchor="center", width=80)
        self.foodtable.column("user_cals",anchor="center",width=80)
        self.foodtable.column("user_prot",anchor="center",width=80)
        self.foodtable.column("user_size",anchor="center",width=80)

        # Setup headings for the table
        self.foodtable.heading("#0",text="",anchor="center")
        self.foodtable.heading("user_food",text="Food",anchor="center")
        self.foodtable.heading("user_cals",text="Calories",anchor="center")
        self.foodtable.heading("user_prot",text="Protein",anchor="center")
        self.foodtable.heading("user_size",text="Serving Size",anchor="center")

        # Get prev 30 data food values from DB
        self.res = self.getfoodhistory()

        # Insert data into table
        self.tempz = 0
        for i in self.res:
            self.foodtable.insert(parent='',index='end',text='',
            values=(i[0],float(i[1]),float(i[2]),float(i[3])),iid=self.tempz)
            self.tempz += 1
        self.foodtable.pack()

        # Return home btn      
        self.backBtn = ttk.Button(
            self,
            text="Back",
            style="big.TButton",
            command=lambda: self.changePage(2))  # ChangePage 1, meaning it will open index 1 of pages list
        self.backBtn.pack(pady=10)
