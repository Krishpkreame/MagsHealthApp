# Import Base Libs
import tkinter as tk
from tkinter import ttk

"""
Make a class for every new page you want to create, this is to better organize your TK pages.
In the class make a function called create which contains widgets(Labels, Images, TextFeilds)
that you want to on that page.
When making widgets ensure to always use 'self.' before the naming the var.
Always use grid, not pack or place
"""
########################## - Program - ##########################


class homepage():  # Home page class
    def create(self):  # Function will create widgets when invoked
        # Get the photo from computer
        self.photo = tk.PhotoImage(file='./img/logo.png')
        # Make a label using the image we got
        self.image_label = ttk.Label(
            self,
            image=self.photo,
        )
        # Place on grid into the window
        self.image_label.grid(
            row=1,
            column=1,
            pady=10)
        # Create a button that will call the changePage call (in the main file)
        self.button = ttk.Button(
            self,
            text="Next Page",
            command=lambda: self.changePage(1))  # ChangePage 1, meaning it will open index 1 of pages list
        # Place on grid into the window
        self.button.grid(
            row=2,
            column=1,
            pady=10)


# no comments u get the idea
class testpage():
    def create(self):
        self.label = ttk.Label(
            self,
            text="Testing",
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


class workoffthis():
    def create(self):
        self.label = ttk.Label(text="Krish Patel")
        self.label.grid(row=1, column=1)
        #
        # CODE HERE
        #
