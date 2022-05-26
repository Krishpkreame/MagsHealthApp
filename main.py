import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.availablePages = [self.page1, self.page2]
        self.page1()

    def changePage(self, nmbr):
        print("Help me lol")
        for widget in self.winfo_children():
            widget.destroy()
        self.availablePages[nmbr]()

    def page1(self):
        self.label = ttk.Label(
            self,
            text="This is page 1",
        ).grid(row=1)
        self.button = ttk.Button(
            self,
            text="To page 2",
            command=lambda: self.changePage(1)
        ).grid(row=2)

    def page2(self):
        self.label = ttk.Label(
            self,
            text="This is page 2 -------------",
        ).grid(row=0)
        self.button = ttk.Button(
            self, text="To page 1", command=lambda: self.changePage(0)).grid(row=1)
        self.entry = ttk.Entry(self)
        self.entry.insert(0, "Entry")
        self.entry.grid(row=2, column=0, padx=15, pady=(0, 10), sticky="ew")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "light")

    app = App(root)
    app.grid()
    root.mainloop()
