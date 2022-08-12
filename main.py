# Date/Time libs
import datetime
import time
# Tkinter libs
import tkinter as tk
from PIL import Image, ImageTk  # putting images into app
from tkinter.messagebox import *
from tkinter import ttk
import tkinter_pages  # - custom
# Database libs
import pymysql
import bcrypt
# Graph Libs
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Extra libaries
from khap_food_api import nutritionInfo
import email_validator
import requests
import random


class App(ttk.Frame):  # App class TKinter
    # Initizlize function
    def __init__(self, parent):
        self.quotesgiturl = """
        https://raw.githubusercontent.com/dwyl/quotes/main/quotes.json"""
        self.currentPage = 0  # Var to keep track of current page
        # SQL DATABASE ----------------------------------
        # Setup sql connection
        self.DBconn = pymysql.connect(
            host="121.98.68.25",
            port=1706,
            user='magsuser',
            passwd='o6Rf@K*#5%sLDt',
            db='MagsHealthApp')
        self.sqlCur = self.DBconn.cursor()
        # Tkinter setup --------------------------------
        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        self.name = "Placeholder"  # Class variables
        # Page list - ADD NEW CLASSES YOU MAKE TO LIST!
        # (pages will be indexed chronologically)
        self.availablePages = [
            tkinter_pages.loginpage,
            tkinter_pages.signpage,
            tkinter_pages.mainpage,
            tkinter_pages.weightForm,
            tkinter_pages.foodForm,
            tkinter_pages.foodHistory]
        # Split into 3 colums
        for i in range(3):
            self.columnconfigure(index=i, weight=1)
        # Show first page on list at start up
        self.changePage(0)

    # Function to get image at certain size
    def getimage(self, name, x, y):
        self.image = Image.open("./img/" + name + ".png")
        self.image = self.image.resize((x, y), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(self.image)  # return resized image

    # Func to quit app
    def quitapp(self):
        global root  # Get root window
        print("Quitting app")
        root.quit()  # quit it

    # Function to change between pages
    def changePage(self, nmbr):
        for widget in self.winfo_children():  # For each widget on scren
            widget.destroy()  # Destory each widget found
        # Run the create function on the desired page
        self.currentPage = nmbr
        self.availablePages[nmbr].create(self)

    # Login func to login and move to next screen``
    def login(self, email, password):
        # SQL - get hashed password for email from DB
        self.sqlCur.execute(
            "SELECT `pswd`,name FROM logininfo WHERE `email`=%s",
            (email.lower()))
        self.sqlpswdresult = self.sqlCur.fetchone()
        # Check if email exists
        if self.sqlpswdresult is not None:
            # Password checking
            # convert hashed DB pswd and user input pswd to bytes
            if bcrypt.checkpw(bytes(password, 'utf-8'),
                              bytes(self.sqlpswdresult[0], 'utf-8')):
                # Save name and email locally as class variables
                self.email = email.lower()
                self.name = self.sqlpswdresult[1]
                print("Correct password\nLogined as", self.name, self.email)
                # Move to homepage
                self.changePage(2)
            else:  # If hashed password dont match
                showwarning(
                    title="Error", message="Incorrect password")
        else:  # If sql email lookup returns nothing
            showerror(
                title="Invalid username",
                message="User does not exist (Wrong email)")

    # Signup func to create new user in db
    def signup(self, name, tempemail, password, confirmPassword):
        # Check if any inputs empty
        for i in [name, tempemail, password, confirmPassword]:
            if i == '':
                showerror(
                    title="Error", message="No fields can be left blank")
                return
        try:
            # Check if email is valid
            email = email_validator.validate_email(tempemail.lower()).email
            # Check if password and confirm password match
            if password == confirmPassword:
                # Hash the password
                self.pswdHashed = bcrypt.hashpw(
                    bytes(password.strip(), 'utf-8'), bcrypt.gensalt())
                # Insert name, email, hashed password into DB as new user
                self.sqlCur.execute("""
                insert into logininfo (name, email, pswd) values (%s, %s, %s)
                """, (name, email, self.pswdHashed))
                # Due to sql being a insert command commit is needed
                self.DBconn.commit()
                print("Successfully signed up")
                self.changePage(0)
        except BaseException as e:
            print(e)
            showwarning(title="Invalid Email", message=e)

    # Graph func will create ./img/graph.png to show on homepage
    def graphInit(self):
        # Sql cmd to get 15 most recent data values for the current user DB
        self.sqlCur.execute("""
            select time,weight
            from data
            where `email`=%s
            order by id desc
            limit 15;""",
                            (self.email))
        result = self.sqlCur.fetchall()
        # Empty lists for graphs
        self.times = []
        self.values = []
        # Go through the data from DB and populate class var lists to them.
        for i in result:
            self.times.append(i[0])
            self.values.append(float(i[1]))
        # Init values for dymanic graph
        self.lowestWeight = 999999
        self.highestWeight = 0
        for x in self.values:  # Go through the weight values
            # If x value lower than the lowest found so far
            # update new lowest value
            if x <= self.lowestWeight:
                self.lowestWeight = x
            # If x value higher than the highest found so far
            # update new highest value
            if x >= self.highestWeight:
                self.highestWeight = x
        if dodarkmode:  # If darkmode then
            # Change plot into figure object, dark mode
            fig = plt.figure(facecolor='#333333')
            # Adjust the graph y limits so that minimal blank shape
            plt.ylim(self.lowestWeight-10, self.highestWeight+10)
            ax = plt.subplot(111)  # Line graph
            # plot values in line graph , darkmode
            ax.plot(self.times, self.values, 'o-', c="#fa5316")
            # Only use day and month shorthand name on x axis (not year)
            ax.xaxis.set_major_formatter(
                mdates.DateFormatter('%b-%d'))
            # Set background to dark color, darkmode
            ax.set_facecolor("#333333")
            # Set x and y axis color , darkmode
            ax.tick_params(axis='x', colors='#d47957')
            ax.tick_params(axis='y', colors='#d47957')
            # Add horizontal grid lines, darkmode
            ax.yaxis.grid(linestyle="--", linewidth=0.3, color="#666666")
            # Change all outlines of graph to color , darkmode
            for i in ['top', 'bottom', 'left', 'right']:
                ax.spines[i].set_color('#736e6c')
            # Save the image file
            fig.savefig('./img/graph.png')
        else:  # Light mode
            fig = plt.figure()  # Change plot into figure object , light mode
            # Adjust the graph y limits so that minimal blank shape, light mode
            plt.ylim(self.lowestWeight-10, self.highestWeight+10)
            ax = plt.subplot(111)  # Line graph, light mode
            ax.plot(self.times, self.values, 'o-')
            # Add horizontal grid lines, darkmode
            ax.yaxis.grid(linestyle="--", linewidth=0.3)
            # Change all outlines of graph to color , darkmode
            for i in ['top', 'bottom', 'left', 'right']:
                ax.spines[i].set_color('#736e6c')
            # Only use day on x axis (not year or month), light mode
            ax.xaxis.set_major_formatter(
                mdates.DateFormatter('%b-%d'))
            # Save the image file
            fig.savefig('./img/graph.png')

    # Weight func to add an entry to DB for tracking weight
    def weightForm(self, weight):
        # Sql cmd to insert new data into the db
        try:
            # Convert texted string to float
            self.weightTemp = float(weight.strip())
            if self.weightTemp <= 0:  # If weight is negative or zero
                raise ValueError("Weight must be positive")
            elif self.weightTemp > 350:
                raise ValueError("Unrealistic weight")
            # Get current date in format Year month date
            self.todayStrtemp = f"{datetime.datetime.now():%Y-%m-%d}"
            # Input correct values into the sql cmd
            # Sql cmd will insert new data values
            # for current date if it doesnt exist
            self.sqlcmd = """
                INSERT INTO data (email, weight, time)
                SELECT '{0}',{1},'{2}' FROM DUAL
                WHERE NOT EXISTS
                (SELECT * FROM data WHERE email='{0}' and time='{2}');
            """.format(self.email, str(self.weightTemp), self.todayStrtemp)
            # Perform insert sql cmd
            self.sqlCur.execute(self.sqlcmd)
            time.sleep(0.05)
            # Input correct values into the sql cmd
            # After the first insert sql cmd is skiped/executed an update
            self.sqlcmd = """
            UPDATE data SET weight = {1} WHERE email = '{0}' and time = '{2}';
            """.format(self.email, str(self.weightTemp), self.todayStrtemp)
            # Perform update sql cmd
            self.sqlCur.execute(self.sqlcmd)
            # Due to update and insert being used commit is needed
            self.DBconn.commit()
            time.sleep(0.05)
            # After the entry is in the DB go back to homepage
            self.changePage(2)
        except ValueError:  # Catch error if float conversion is not possible
            showerror(
                title="Invalid value",
                message="Invalid weight (whole positive or decimal value)")

    # Food func to add an entry to DB for calorie counting
    def foodForm(self, query):
        try:
            # Food API --------------------------------
            self.foodapi = nutritionInfo()  # make new class instance
            # Make a new query using foodapi, and find nutr of wanted food
            self.tempData = self.foodapi.makequery(query)
            # Set the button text to `confirm` to ask user if food is correct
            self.btnStr.set("Confirm?")
            # Set a label's text so the amount of food and food name
            # so ensure user food is correct
            self.confLblStr.set(
                "Are you sure you want: {}g {}?".format(
                    self.tempData["serving_size_g"],
                    self.tempData["name"]))
            # Confirm check
            if self.prevEntry == self.tempData["name"]:
                # Add all food nutrition we want into the database
                self.sqlCur.execute("""
                insert into food (email, food, calories, servingsize, protein)
                values (%s, %s, %s, %s, %s)""", (
                    self.email,
                    self.tempData['name'],
                    self.tempData['calories'],
                    self.tempData['serving_size_g'],
                    self.tempData['protein_g']))
                # Commit the DB changes
                self.DBconn.commit()
                time.sleep(0.05)
                # After the entry is in the DB go back to homepage
                self.changePage(2)
            # After if statment set the var prevEntry to what the user wrote
            self.prevEntry = self.tempData["name"]
        except ValueError:
            # If what the user wrote isnt a food show error box
            showerror(
                title="Invalid value(s)", message="Invalid values entered.")

    # Function to get past 30 food entries for a user
    def getfoodhistory(self):
        # Sql cmd to get most recent data values for the current user from DB
        self.sqlCur.execute("""
            select food,calories,protein,servingsize
            from food
            where `email`=%s
            order by id desc
            limit 30;""",
                            (self.email))
        # Get all results
        foodresult = self.sqlCur.fetchall()
        return foodresult  # and return them

    # Func to get a random qoute for user
    def qouteoftheday(self):
        # Create a random seed based on the date and
        # the first and last letters of user's name.
        self.currentdate = str(datetime.datetime.now())[
            :10]  # date only (no time)
        self.currentdate = self.currentdate + self.name[0] + self.name[-1]
        print(self.currentdate, "is the seed")  # print seed
        random.seed(self.currentdate)  # Set random lib seed to users seed
        # Using requests, get a random quote from the github repo json file
        self.quoteRepo = requests.get(self.quotesgiturl).json()
        self.randomQuoteIndex = random.randint(0, len(self.quoteRepo))
        # return just text
        return self.quoteRepo[self.randomQuoteIndex]['text']
# OUTSIDE CLASS
# -----------------------------------------------------


def toggleTheme(reloadNmbr):  # toggle theme to switch themes, and reload page
    global dodarkmode, app  # Access global dodarkmode bool and app instance
    if dodarkmode:  # If dark mode is enabled
        root.tk.call("set_theme", "light")  # make it light mode
        loadstyles()  # Load styles
        dodarkmode = not dodarkmode  # Change bool to opposite
        # Change image on toggle button to light mode img
        themetogg.config(image=lighton, activebackground='white')
        app.changePage(reloadNmbr)  # Reload page so new styles apply
    else:
        root.tk.call("set_theme", "dark")  # make it dark mode
        loadstyles()  # Loadstyles
        dodarkmode = not dodarkmode  # Change bool to opposite
        # Change image on toggle button to dark mode img
        themetogg.config(image=darkon, activebackground='gray')
        app.changePage(reloadNmbr)  # Reload page so new styles apply


def loadstyles():  # Func to load styles after theme change
    global appstyles  # access the global styles
    appstyles.configure('small.TButton', font=(None, 7))  # small button
    appstyles.configure('big.TButton', font=(None, 18))  # big button


dodarkmode = True  # Bool for darkmode

if __name__ == "__main__":  # If this file is run directly, run the code
    try:  # Run the following code
        root = tk.Tk()  # Create a window
        root.title("Khap")  # Add title
        appstyles = ttk.Style()  # make app empty styles
        root.tk.call("source", "azure.tcl")  # Add the azure theme
        root.tk.call("set_theme", "dark")  # make it dark mode - morbin time
        loadstyles()
        app = App(root)  # Link the App and window we made
        app.pack(fill="both", expand=True)  # Fill window
        # Dark mode switch -----------------------
        # Image for dark mode switch
        darkon = app.getimage("themedark", 32, 16)
        # Image for light mode switch
        lighton = app.getimage("themelight", 32, 16)
        # Create button with dark mode deflaut
        themetogg = tk.Button(
            bd=0, image=darkon,
            command=lambda: toggleTheme(app.currentPage),
            highlightthickness=0, relief="flat", borderwidth=0)
        # Place on very top left on window
        themetogg.place(x=-1, y=-1, width=32, height=16, anchor='nw')
        root.mainloop()  # Run the app
    except Exception as e:  # Catch any other errors
        # show error screen and stop program
        showwarning(title="Fatal Error", message=e)
        input(e)  # stop program
