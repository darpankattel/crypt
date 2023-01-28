import tkinter as tk
import config


class BaseUI:
    def __init__(self, title=config.FULL_APP_NAME, size="full"):
        self.root = tk.Tk()
        self.root.title(title)
        if size == "full":
            self.root.state("zoomed")
            self.root.minsize(1000, 800)
        elif size == "medium":
            self.root.geometry("800x600")
            self.root.minsize(800, 600)
        elif size == "small":
            self.root.geometry("600x500")
            self.root.minsize(600, 500)
        self.root.iconbitmap("resources/images/icon.ico")
        self.root.mainloop()
