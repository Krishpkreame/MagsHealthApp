# Base libaries
import datetime
import tkinter as tk
from tkinter import ttk
import pymysql
import bcrypt
import time
import matplotlib.pyplot as plt

# Import pages
import tkPages


class App(ttk.Frame):
    # Initizlize function
    def __init__(self, parent):
        # Setup sql connection
        self.conn = pymysql.connect(
            host='121.98.68.25',
            port=1706,
            user='appuser',
            passwd='o6Rf@K*#5%sLDt',
            db='MagsHealthApp')
        self.cur = self.conn.cursor()
        # Setup some styling
        styl = ttk.Style()
        styl.configure('small.TButton', font=(None, 7))
        styl.configure('big.TButton', font=(None, 18))
        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        # Page list - ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
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
    def login(self, email, password):  # ! Add comments
        # DB sql cmd
        self.cur.execute(
            "SELECT `pswdHash` FROM login WHERE `email`=%s", (email))
        result = self.cur.fetchone()
        # Check if email exists
        if result is not None:
            # Password checking
            if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(result[0], 'utf-8')):
                print("Correct password")
                # Save email locally
                self.email = email
                self.changePage(2)
            else:
                print("Incorrect password")

    # Signup func to create new user in db
    def signup(self, name, email, password, confirmPassword):  # ! Add comments
        # Check if any inputs empty
        if name != '' and email != '' and password != '' and confirmPassword != '':
            # Check if values are valid
            if password == confirmPassword:
                print("Password matches")
                # Hash password
                self.hashed = bcrypt.hashpw(
                    bytes(password.strip(), 'utf-8'), bcrypt.gensalt())
                print(self.hashed)
                # Insert into DB
                self.sqlcmd = """
                insert into login (name, email, pswdHash) values (%s, %s, %s)"""
                self.cur.execute(self.sqlcmd, (name, email, self.hashed))
                self.conn.commit()

    #! Temp meathod
    def makegraph(self):
        # Sql cmd to get recent data values from the current user
        self.cur.execute(
            """
            select time,weight
            from dataTable
            where `email`=%s
            order by id desc
            limit 3;""",
            (self.email))
        result = self.cur.fetchall()
        self.times = []
        self.values = []

        for i in result:
            self.times.append(i[0])
            self.values.append(float(i[1]))

        print(self.times)
        print(self.values)

        fig = plt.figure()
        ax = plt.subplot(111)
        ax.plot(self.times, self.values, label='$y = numbers')
        plt.title('Legend inside')
        ax.legend()
        # plt.show()

        fig.savefig('./img/graph.png')
        self.changePage(0)

    def inputForm(self, weight):  # ! Add comments
        # Sql cmd to insert new data into the db
        try:
            self.weighttemp = float(weight.strip())
            self.todayStrtemp = f"{datetime.datetime.now():%Y-%m-%d}"
            self.sqlcmd = """
                INSERT INTO dataTable (email, weight, time) 
                SELECT '{0}',{1},'{2}' FROM DUAL 
                WHERE NOT EXISTS (SELECT * FROM dataTable WHERE email='{0}' and time='{2}');
            """.format(self.email, str(self.weighttemp), self.todayStrtemp)
            self.cur.execute(self.sqlcmd)
            time.sleep(0.05)
            self.sqlcmd = """
                UPDATE dataTable 
                SET
                    weight = {1}
                WHERE
                    email = '{0}' and time = '{2}';
            """.format(self.email, str(self.weighttemp), self.todayStrtemp)
            self.cur.execute(self.sqlcmd)
            self.conn.commit()
            time.sleep(1)
            self.changePage(2)
        except ValueError:
            print("Invalid weight")


if __name__ == "__main__":  # If this file is run directly, run the following code
    root = tk.Tk()  # Create a window
    root.title("Khap")  # Add title
    root.tk.call("source", "azure.tcl")  # Add the azure theme
    root.tk.call("set_theme", "dark")  # make it dark mode - morbin time
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app
