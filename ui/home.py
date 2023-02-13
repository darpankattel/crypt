import tkinter as tk
import config

from tkinter.messagebox import showinfo


class HomeUI(tk.Tk):
    """
    This is the main UI class of the app. The instance of this class is the main app.
    """

    def __init__(self, title=config.FULL_APP_NAME, size="full"):
        # initializing the tk.Tk() constructor
        super().__init__()

        # here self is the root object, i.e; root = tk.Tk() as in normal sense
        self.title(title)

        # size and position configuration for the app instance
        if size == "full":
            self.state("zoomed")
            self.minsize(1000, 800)
        elif size == "medium":
            self.geometry("800x600")
            self.minsize(800, 600)
        elif size == "small":
            self.geometry("600x500")
            self.minsize(600, 500)

        # setting an icon bitmap for the app
        self.iconbitmap("resources/images/icon.ico")

        # TODO Everything other then basic configuration will reside after here

        self.label = tk.Label(self, text='Hello, Bishnu Badu!')
        self.label.pack()

        # button
        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        """
        TODO
        1. Show a initial login/signin UI for the user to login.
        2. Prompt necessary screens like, password not matching, loading, etc. as per need
        3. If the user is new:
            a. add him to the database
            b. show necessary ui as per design
          else:
            a. take him to the main ui
        4. Initial fetch to the database using the Django Model
        5. Adding interface for the use for CRUD operations and also export and import operation as per need.
        5. Updating the screen as per the need.


        FAQs
        1. WHAT ARE WE GOING TO USE FROM TKINTER (SOME ADVANCE ELEMENTS)?
        => TopLevel Widget for creating a new top level window, threading library for doing some tasks parallely, drag and drop func., event handeling, animation, etc..

        2. WHAT IS THE BASIC IDEA OF OUR PROJECT?
        => The basic idea is to have a simple app where we could drag or kind of upload a file or a folder to encrypt into, as a result the original file/folder would be transferred to our vault, and can only be decrypted by the person who is logged in and is entitled to the file or folder. Other functionalitites are, deletion of the same, exporting(moving it out from our app), etc..
        """

        # WARNING: calling the mainloop method here is un-necessary and may cause unwanted behaviors
        # self.mainloop()

    def button_clicked(self):
        showinfo(title='My Title',
                 message='Hello, Baduman!\nDo you have a marker? 😅')
