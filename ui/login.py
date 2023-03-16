import tkinter as tk
from logic import CryptAuth
from tkinter import messagebox
from functions import clearinside
import config


class LoginUI:
    def __init__(self, master, auth: CryptAuth, on_login_success, on_signup_click):
        self.master = master
        self.auth = auth
        self.on_login_success = on_login_success
        self.on_signup_click = on_signup_click

        self.master.config(bg="#C399CC")
        self.master.geometry("1200x800")
        self.master.minsize(800, 600)
        self.master.iconbitmap("resources/images/icon.ico")
        self.master.title(config.FULL_APP_NAME)

        self.main_container = tk.Frame(self.master)
        self.main_container.pack(fill="both")
        self.main_container.config(bg="#C399CC")
        # for crypt text
        self.frame_left = tk.Frame(self.main_container, bg="#C399CC")
        self.frame_left.pack(side="left", fill="y", padx=10, pady=10)

        self.canvas = tk.Canvas(
            self.frame_left, highlightthickness=0, bg="#C399CC")
        self.canvas.pack(side="left", fill="both", padx=(20, 0))

        # Draw triangle on canvas
        # self.canvas.create_polygon(0, 80, 350, 150, 0, 775, fill="white")
        self.canvas.create_polygon(
            0, 80, 1000, 0, 150, 200, 500, 0, 0, 775, fill="#cccccc", tags="polygon")

        # Add image to the left of the triangle
        self.photo1 = tk.PhotoImage(
            file="resources/images/main_logo.png")
        self.photo1 = self.photo1.subsample(2, 2)
        self.image_item = self.canvas.create_image(130, 150, image=self.photo1)

        # Add text to the right of the triangle
        self.canvas.create_text(270, 150, text="Crypt",
                                font=("sunken", 27, "bold"))
        self.canvas.create_text(
            170, 220, text="Your personal data are more important.", font=("sunken", 12))
        self.canvas.create_text(
            170, 240, text="Secure your personal photos,videos,", font=("sunken", 12))
        self.canvas.create_text(
            170, 260, text="documents,voice messages with us.", font=("sunken", 12))

        # Create a frame to hold the widgets in right side of the window
        self.right_frame = tk.Frame(self.main_container, bg="#C399CC")
        self.right_frame.pack(anchor="e", padx=(0, 200))

        self.photo = tk.PhotoImage(
            file="resources/images/userphoto.png")
        self.label = tk.Label(self.right_frame, image=self.photo, bg="#C399CC")
        self.label.grid(row=0, column=1, pady=(25, 0))

        self.text_label = tk.Label(self.right_frame, text="Login", bg="#C399CC", fg="white", font=(
            "sunken", 27, "bold"), anchor="n")
        self.text_label.grid(row=1, column=1, pady=(0, 25))

        # Create labels for username and password

        tk.Label(self.right_frame, text="Username:", bg="#C399CC", fg="white", font=(
            "Arial", 15)).grid(row=2, column=0, pady=10, sticky="e")
        tk.Label(self.right_frame, text="Password:", bg="#C399CC", fg="white", font=(
            "Arial", 15)).grid(row=3, column=0, pady=10, sticky="e")

        # Create entry widgets for username and password
        self.username_entry = tk.Entry(
            self.right_frame, font=("Arial", 19), width=30)
        self.username_entry.grid(
            row=2, column=1, pady=10, ipady=10, sticky="w")
        self.password_entry = tk.Entry(
            self.right_frame, show="*", font=("Arial", 19), width=30)
        self.password_entry.grid(
            row=3, column=1, pady=10, ipady=10, sticky="w")

        # Forget password
        self.forget_button = tk.Button(self.right_frame, text="Forgot Password?", bg="#C399CC", fg="white", font=(
            "Arial", 13), bd=0, activebackground="#C399CC", activeforeground="white", cursor="hand2")
        self.forget_button.grid(row=4, column=1, sticky='e', pady=5)

        # Remember me
        self.remeber_button = tk.Checkbutton(self.right_frame, text="Remember Me", bg="#C399CC", fg="white", font=(
            "Arial", 13), bd=0, activebackground="#C399CC", activeforeground="white", cursor="hand2")
        self.remeber_button.grid(row=4, column=1, sticky='w', pady=5)

        # Create a button for login
        self.btn_photo = tk.PhotoImage(
            file="resources/images/loginlight.png")
        self.login_button = tk.Button(self.right_frame, image=self.btn_photo, bg="#C399CC", fg="#862d86",
                                      bd=0, activebackground="#C399CC",  activeforeground="#862d86", cursor="hand2", width=350, height=60, command=self.login_click)
        self.login_button.grid(row=5, column=1, pady=10)

        # Create a hyperlink for sign up
        self.signup_label = tk.Button(self.right_frame, text="Don't have an account? Sign up", bg="#C399CC", fg="white", font=(
            "Arial", 13, "underline"), bd=0, activebackground="#C399CC", activeforeground="white", cursor="hand2", command=self.signup_click)
        self.signup_label.grid(row=6, column=1)

    def login_click(self):
        print(self.username_entry.get(), self.password_entry.get())
        if self.auth.login(self.username_entry.get(), self.password_entry.get()):
            self.on_login_success()
        else:
            messagebox.showerror(
                "Couldn't log in", "Looks like the username or the password you provided didn't match with our database. Try again with changes.")

    def signup_click(self):
        self.main_container.destroy()
        self.on_signup_click()

    # def destroy(self):
    #     self.m


# import tkinter as tk
# import config


# class HomeUI(tk.Tk):
#     """
#     This is the main UI class of the app. The instance of this class is the main app.
#     """

#     def __init__(self, title=config.FULL_APP_NAME, size="full"):
#         # initializing the tk.Tk() constructor
#         super().__init__()

#         # here self is the root object, i.e; root = tk.Tk() as in normal sense
#         self.title(title)

#         # size and position configuration for the app instance
#         if size == "full":
#             self.state("zoomed")
#             self.minsize(1000, 800)
#         elif size == "medium":
#             self.geometry("800x600")
#             self.minsize(800, 600)
#         elif size == "small":
#             self.geometry("600x500")
#             self.minsize(600, 500)

#         # setting an icon bitmap for the app
#         self.iconbitmap("resources/images/icon.ico")

#         # TODO Everything other then basic configuration will reside after here
#         self.configure(bg="#C399CC")

#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         # if self.auth.login(username, password):
#         self.on_login_success()

#     def destroy(self):
#         self.frame.destroy()
