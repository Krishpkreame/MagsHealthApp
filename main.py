# Base libaries
import tkinter as tk
from tkinter import ttk
# Import pages
import tkPages


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        #
        # Page list
        # ADD NEW CLASSES YOU MAKE TO LIST!  (pages will be indexed chronologically)
        self.availablePages = [
            tkPages.homepage,
            tkPages.testpage,
            tkPages.workoffthis]
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


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Khap")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
