import tkinter as tk
from tkinter import ttk
import tkPages
# temp packages
import threading
import time


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)  # initialize the superclass (frame)
        # Vars -
        self.started = False
        self.count = 0
        # Page list
        self.availablePages = [
            tkPages.homepage,
            tkPages.page1]
        # Split into 3 colums
        for a in [0, 1, 2]:
            self.columnconfigure(index=a, weight=1)
        # Show first page on list at start up
        self.availablePages[0].show(self)

    def changePage(self, nmbr):
        for widget in self.winfo_children():
            widget.destroy()
        self.availablePages[nmbr].show(self)

    def timer(self):
        time.sleep(3)
        self.label.config(text=str(self.count))

    def cpstest(self):
        if(self.started == False):
            self.label.config(text="CLICK!!!")
            self.started = True
            threading.Thread(target=self.timer).start()
        self.count += 1


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Khap")
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    app = App(root)
    app.pack(fill="both", expand=True)
    root.mainloop()
