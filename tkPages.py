from re import S
import tkinter as tk
from tkinter import ttk


class homepage():
    def show(self):
        self.photo = tk.PhotoImage(file='./img/logo.png')
        self.image_label = ttk.Label(
            self,
            image=self.photo,
            padding=5
        )
        self.image_label.grid(row=1, column=1, padx=15, pady=10)
        self.button = ttk.Button(
            self, text="Next Page", command=lambda: self.changePage(1))
        self.button.grid(row=2, column=1, padx=15, pady=10)


class page1():
    def show(self):
        self.label = ttk.Label(
            self,
            text="Logo",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=1, pady=10)
        self.button = ttk.Button(
            self, text="Last Page", command=lambda: self.changePage(0))
        self.button.grid(row=2, column=1, pady=10)
        self.button = ttk.Button(
            self, text="SetText", command=lambda: self.cpstest())
        self.button.grid(row=3, column=1, padx=15, pady=10)
