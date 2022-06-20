# Base libaries
import tkinter as tk
from tkinter import ttk
import pymysql
import bcrypt
# Import pages
import tkPages


class App(ttk.Frame):
    def __init__(self, parent):
        # Setup sql connection
        self.conn = pymysql.connect(host='sql6.freemysqlhosting.net', port=3306,
                                    user='sql6500321', passwd='fihcAN1pcZ', db='sql6500321')
        self.cur = self.conn.cursor()
        # Setup some styling
        s = ttk.Style()
        s.configure('small.TButton', font=(None, 7))
        s.configure('big.TButton', font=(None, 18))

        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        #
        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
        self.availablePages = [
            tkPages.loginpage,
            tkPages.signpage,
            tkPages.mainpage]
        #
        #
        # Split into 3 colums
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        # Show first page on list at start up
        self.availablePages[0].create(self)

    # Function to change between pages
    def changePage(self, nmbr):
        for widget in self.winfo_children():  # For each widget on scren
            widget.destroy()  # Destory each widget found
        #
        #
        # Run the create function on the desired page
        self.availablePages[nmbr].create(self)

    # Login func to login and move to next screen
    def login(self, email, password):  # ! Add comments
        # Save email locally
        self.email = email
        # DB sql cmd
        self.cur.execute(
            "SELECT `pswdHash` FROM MagsHealthApp WHERE `email`=%s", (email))
        result = self.cur.fetchone()
        #
        # Check if email exists
        if result is not None:
            # Password checking
            if bcrypt.checkpw(bytes(password, 'utf-8'), bytes(result[0], 'utf-8')):
                print("Correct password")
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
                self.sqlcmd = """insert into MagsHealthApp (name, email, pswdHash, weight)
                        values (%s, %s, %s, %s)
                """
                self.cur.execute(self.sqlcmd, (name, email, self.hashed, 0))
                self.conn.commit()

    def makegraph(self):
        # DB sql cmd
        self.cur.execute(
            "SELECT * FROM dataTable WHERE `email`=%s", (self.email))
        result = self.cur.fetchall()
        print(result)


if __name__ == "__main__":  # If this file is run directly, run the following code
    root = tk.Tk()  # Create a window
    root.title("Khap")  # Add title
    root.tk.call("source", "azure.tcl")  # Add the azure theme
    root.tk.call("set_theme", "dark")  # make it dark mode - morbin time
    app = App(root)  # Link the App and window we made
    app.pack(fill="both", expand=True)  # Allow resizing
    root.mainloop()  # Run the app
