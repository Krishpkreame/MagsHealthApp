import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.availablePages = [self.page1, self.page2]
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=1, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.page1()

    def changePage(self, nmbr):
        print("Help me lol")
        for widget in self.winfo_children():
            widget.destroy()
        self.availablePages[nmbr]()

    def page1(self):
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

    def page2(self):
        self.label = ttk.Label(
            self,
            text="Logo",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=1, pady=10)
        self.button = ttk.Button(
            self, text="Last Page", command=lambda: self.changePage(0))
        self.button.grid(row=2, column=1, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    root.mainloop()
