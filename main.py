# Base libaries
import datetime
import time
import tkinter as tk
from tkinter import ttk
import pymysql
import bcrypt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# Food API
from PYfoodapi import *
# Import pages
import tkPages


class App(ttk.Frame):
    # Initizlize function
    def __init__(self, parent):
        # SQL DATABASE ----------------------------------
        # Setup sql connection
        self.DBconn = pymysql.connect(
            host='121.98.68.25',
            port=1706,
            user='appuser',
            passwd='o6Rf@K*#5%sLDt',
            db='MagsHealthApp')
        self.sqlCur = self.DBconn.cursor()
        # Tkinter setup --------------------------------
        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        self.name = "Placeholder"  # Class variables
        # Setup some styling
        styl = ttk.Style()
        styl.configure('small.TButton', font=(None, 7))
        styl.configure('big.TButton', font=(None, 18))
        # Page list - ADD NEW CLASSES YOU MAKE TO LIST!
        # (pages will be indexed chronologically)
        self.availablePages = [
            tkPages.loginpage,
            tkPages.signpage,
            tkPages.mainpage,
            tkPages.inputForm]
        # Split into 3 colums
        for i in range(3):
            self.columnconfigure(index=i, weight=1)
        # Show first page on list at start up
        self.availablePages[0].create(self)

    # Function to change between pages
    def changePage(self, nmbr):
        for widget in self.winfo_children():  # For each widget on scren
            widget.destroy()  # Destory each widget found
        # Run the create function on the desired page
        self.availablePages[nmbr].create(self)

    # Login func to login and move to next screen
    def login(self, email, password):
        # SQL - get hashed password for email from DB
        self.sqlCur.execute(
            "SELECT `pswdHash`,name FROM login WHERE `email`=%s", (email))
        self.sqlpswdresult = self.sqlCur.fetchone()
        # Check if email exists
        if self.sqlpswdresult is not None:
            # Password checking --- convert hashed DB pswd and user input pswd to bytes
            if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(self.sqlpswdresult[0], 'utf-8')):
                # Save name and email locally as class variables
                self.email = email
                self.name = self.sqlpswdresult[1]
                print("Correct password\nLogined as", self.name, self.email)
                # Move to homepage
                self.changePage(2)
            else:  # If hashed password dont match
                print("Error: Incorrect password")
        else:  # If sql email lookup returns nothing
            print("Error: User does not exist (Wrong email)")

    # Signup func to create new user in db
    def signup(self, name, email, password, confirmPassword):
        # Check if any inputs empty
        if name != '' and email != '' and password != '' and confirmPassword != '':
            # Check if password and confirm password match
            if password == confirmPassword:
                print("Passwords matches")
                # Hash the password
                self.pswdHashed = bcrypt.hashpw(
                    bytes(password.strip(), 'utf-8'), bcrypt.gensalt())
                # Insert name, email, hashed password into DB as new user
                self.sqlCur.execute("""
                insert into login (name, email, pswdHash) values (%s, %s, %s)""",
                                    (name, email, self.pswdHashed))
                # Due to sql being a insert command commit is needed
                self.DBconn.commit()
        else:  # If any inputs are empty
            print("Error: No fields can be left blank")

    def graphInit(self):
        # Sql cmd to get 15 most recent data values for the current user from DB
        self.sqlCur.execute("""
            select time,weight
            from dataTable
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
            # If x value lower than the lowest found so far, update new lowest value
            if x <= self.lowestWeight:
                self.lowestWeight = x
            # If x value higher than the highest found so far, update new highest value
            if x >= self.highestWeight:
                self.highestWeight = x
        fig = plt.figure()  # Change plot into figure object
        # Adjust the graph y limits so that minimal blank shape
        plt.ylim(self.lowestWeight-10, self.highestWeight+10)
        ax = plt.subplot(111)  # Line graph
        ax.plot(self.times, self.values)  # plot the values
        # Only use day on x axis (not year or month)
        ax.xaxis.set_major_formatter(
            mdates.DateFormatter('%b-%d'))
        # Save the image file
        fig.savefig('./img/graph.png')

    def inputForm(self, weight):
        # Sql cmd to insert new data into the db
        try:
            # Convert texted string to float
            self.weightTemp = float(weight.strip())
            if self.weightTemp <= 0:  # If weight is negative or zero
                raise ValueError  # Raise value error
            # Get current date in format Year month date
            self.todayStrtemp = f"{datetime.datetime.now():%Y-%m-%d}"
            # Input correct values into the sql cmd
            # Sql cmd will insert new data values for current date if it doesnt exist
            self.sqlcmd = """
                INSERT INTO dataTable (email, weight, time)
                SELECT '{0}',{1},'{2}' FROM DUAL
                WHERE NOT EXISTS (SELECT * FROM dataTable WHERE email='{0}' and time='{2}');
            """.format(self.email, str(self.weightTemp), self.todayStrtemp)
            # Perform insert sql cmd
            self.sqlCur.execute(self.sqlcmd)
            time.sleep(0.05)
            # Input correct values into the sql cmd
            # After the first insert sql cmd is skiped/executed an update cmd will run
            # This is to update the value of that day if after the first insert is skipped
            self.sqlcmd = """
                UPDATE dataTable SET weight = {1} WHERE email = '{0}' and time = '{2}';
            """.format(self.email, str(self.weightTemp), self.todayStrtemp)
            # Perform update sql cmd
            self.sqlCur.execute(self.sqlcmd)
            # Due to update and insert being used commit is needed
            self.DBconn.commit()
            time.sleep(0.05)
            # After the entry is in the DB go back to homepage
            self.changePage(2)
        except ValueError:  # Catch error if float conversion is not possible
            print("Error: Invalid weight (whole positive value or decimal only)")


if __name__ == "__main__":  # If this file is run directly, run the following code
    try:  # Run the following code
        root = tk.Tk()  # Create a window
        root.title("Khap")  # Add title
        root.tk.call("source", "azure.tcl")  # Add the azure theme
        root.tk.call("set_theme", "dark")  # make it dark mode - morbin time
        app = App(root)  # Link the App and window we made
        app.pack(fill="both", expand=True)  # Fill window
        root.mainloop()  # Run the app
    except Exception as e:  # Catch any other errors
        input(e)  # Stop program and print error message
