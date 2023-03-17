"""
WARNING: Donot change the position of the below code
"""
import sys
import os
import django

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'orm')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
django.setup()

# every code reside below this
import tkinter as tk
from logic.auth import CryptAuth
from ui import HomeUI, LoginUI, SignUpUI

class MainUI:
    def __init__(self, login_master) -> None:
        self.login_master = login_master
        self.login_master.title("Loading...")
        self.auth = CryptAuth()
        self.show_login_ui()
        # self.auth.login("username", "Password")
        # self.show_home_ui()

    def show_home_ui(self):
        self.login_master.destroy()
        self.home_ui = HomeUI(self.auth)

    def show_signup_ui(self):
        self.signup_ui = SignUpUI(
            self.login_master, self.auth, self.show_login_ui, self.show_login_ui)

    def show_login_ui(self):
        self.login_ui = LoginUI(
            self.login_master, self.auth, self.show_home_ui, self.show_signup_ui)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainUI(root)
    root.mainloop()
