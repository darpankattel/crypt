import tkinter as tk
import config
import webbrowser
from tkinter.messagebox import showinfo
from tkinter import filedialog, simpledialog, scrolledtext, ttk
from PIL import Image, ImageTk
from .tooltip import CreateToolTip
from logic import CryptAuth
from tkinter import messagebox
from logic import Sort, Vault
from functions import get_file_extension, get_formatted_date
from data import EncryptedFileTree


class HomeUI(tk.Tk):
    """
    This is the main UI class of the app. The instance of this class is the main app.
    """

    def __init__(self, auth: CryptAuth, title=config.FULL_APP_NAME, size="full"):
        super().__init__()
        self.auth = auth
        self.myvault = Vault(self.auth.get_current_user())

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

        if not self.auth.get_current_user().has_toured:
            self.ask_tour_and_directory()

        # Create navbar frame
        self.navbar = tk.Frame(self, height=20, bg="black")
        self.navbar.pack(fill="x")

        # add logo and text to navbar
        self.logo = tk.PhotoImage(file="resources/images/main_logo.png")
        self.logo = self.logo.subsample(5, 5)
        self.logo_label = tk.Label(self.navbar, image=self.logo, bg="black")
        self.logo_label.pack(side="left", padx=20)

        self.text_label = tk.Label(
            self.navbar, text="Crypt", bg="black", fg="white", font=("Arial", 16, "bold"))
        self.text_label.pack(side="left", padx=(0, 10))

        # add search bar to navbar
        self.search_entry = tk.Entry(self.navbar, bg="white", fg="black", font=(
            "Arial", 14), width=50)
        self.search_entry.insert(0, "Search")
        self.search_entry.place(relx=0.5, rely=0.5, anchor="center")
        self.search_entry.config(insertbackground="white")
        self.search_entry.config(highlightthickness=1)
        self.search_entry.config(bd=1)

        # add icons to navbar
        self.icon1 = tk.PhotoImage(file="resources/images/ques.png")
        self.icon1_label = tk.Button(
            self.navbar, image=self.icon1, bg="black", bd=0, activebackground="black", cursor="hand2")
        self.icon1_label.pack(side="right", padx=15, pady=5)

        self.icon2 = tk.PhotoImage(file="resources/images/gear.png")
        self.icon2_label = tk.Button(
            self.navbar, image=self.icon2, bg="black", bd=0, activebackground="black", cursor="hand2")
        self.icon2_label.pack(side="right", padx=15, pady=5)

        self.icon3 = tk.PhotoImage(file="resources/images/vector.png")
        self.icon3_label = tk.Button(
            self.navbar, image=self.icon3, bg="black", bd=0, activebackground="black", cursor="hand2", command=self.show_profile)
        self.icon3_label.pack(side="right", padx=15, pady=5)

        CreateToolTip(self.icon3_label, auth.get_current_user().full_name)

        self.configure(background="white")

        # create the left frame
        self.left_frame = tk.Frame(self, bg="#C399CC")
        self.left_frame.pack(side="left", fill="y")

        self.advert_frame = tk.Frame(self.left_frame, bg="#C399CC")
        self.advert_frame.pack(side="top", fill="x")

        self.hamburgerimg = tk.PhotoImage(file="resources/images/hambur.png")
        self.hamburgerbtn = tk.Button(self.advert_frame, image=self.hamburgerimg, bg="#C399CC",
                                      bd=0, cursor="hand2", foreground="black", activebackground="#C399CC")
        self.hamburgerbtn.grid(row=0, column=0, padx=12)

        self.menu_txt = tk.Label(self.advert_frame, text="Menu", font=(
            "Arial", 18, "bold"), bg="#C399CC", foreground="black")
        self.menu_txt.grid(row=0, column=1)

        self.homeimg = tk.PhotoImage(file="resources/images/home-button.png")
        self.homebtn = tk.Button(self.left_frame, image=self.homeimg, bg="#C399CC",
                                 bd=0, cursor="hand2", foreground="black", activebackground="#C399CC", command=self.set_home)
        self.homebtn.pack(side="top", pady=10, padx=12)

        self.voiceimg = tk.PhotoImage(file="resources/images/voice.png")
        self.voicebtn = tk.Button(self.left_frame, image=self.voiceimg, bg="#C399CC",
                                  bd=0, cursor="hand2", foreground="black", activebackground="#C399CC", command=self.set_voice)
        self.voicebtn.pack(side="top", pady=10, padx=12)

        self.videoimg = tk.PhotoImage(file="resources/images/videos.png")
        self.videobtn = tk.Button(self.left_frame, image=self.videoimg, bg="#C399CC",
                                  bd=0, cursor="hand2", foreground="black", activebackground="#C399CC", command=self.set_video)
        self.videobtn.pack(side="top", pady=10, padx=12)

        self.pictureimg = tk.PhotoImage(file="resources/images/pictures.png")
        self.picturebtn = tk.Button(self.left_frame, image=self.pictureimg, bg="#C399CC",
                                    bd=0, cursor="hand2", foreground="black", activebackground="#C399CC", command=self.set_picture)
        self.picturebtn.pack(side="top", pady=10, padx=12)

        self.documentimg = tk.PhotoImage(file="resources/images/document.png")
        self.documentbtn = tk.Button(self.left_frame, image=self.documentimg, bg="#C399CC",
                                     bd=0, cursor="hand2", foreground="black", activebackground="#C399CC", command=self.set_document)
        self.documentbtn.pack(side="top", pady=10, padx=12)

        self.label_abt = tk.Button(self.left_frame, text="About us", font=(
            "SUNKEN", 18), bg="#C399CC", foreground="black", activebackground="#C399CC", bd=0, cursor="hand2", command=self.show_about_us)
        self.label_abt.pack(side="bottom", pady=(0, 10))

        self.label_logout = tk.Button(self.left_frame, text="Logout", font=(
            "SUNKEN", 18), bg="#C399CC", foreground="black", activebackground="#C399CC", bd=0, cursor="hand2", command=self.logout)
        self.label_logout.pack(side="bottom", pady=(0, 30))

        self.top_controls_container = tk.Frame(self, height=30, bg="white")
        self.top_controls_container.pack(
            fill="x", side="top", pady=10, padx=12)

        # Create breadcrumb frame
        self.breadcrumb = tk.Frame(
            self.top_controls_container, height=30, bg="white")
        self.breadcrumb.pack(fill="y", side="left")
        # Add each string in breadcrumb list as a Label to the breadcrumb bar
        self.set_breadcrumb()

        self.top_controls = tk.Frame(self.top_controls_container, bg="white")
        self.top_controls.pack(fill="both", side="right")

        self.add_image = tk.PhotoImage(
            file="resources/images/add_button.png")
        self.three_dots_image = tk.PhotoImage(
            file="resources/images/three_dots.png")
        self.three_dots_button = tk.Button(self.top_controls, image=self.three_dots_image, bg="white", bd=0,
                                           cursor="hand2", foreground="black", activebackground="white")
        self.add_button = tk.Button(self.top_controls, image=self.add_image, bg="white",
                                    bd=0, cursor="hand2", foreground="black", activebackground="white")
        self.three_dots_button.pack(side="left", pady=2)
        self.add_button.pack()

        context_menu = tk.Menu(self.master, tearoff=0)
        options_menu = tk.Menu(self.master, tearoff=0)
        context_options = [
            {"label": "Create New Folder", "value": "create"},
            {"label": "Add Folder", "value": "add-folder"},
            {"label": "Add File", "value": "add-file"}
        ]
        sorting_options = [
            {"label": "Sort By Name", "value": "name", "type": "sort_by"},
            {"label": "Sort By Date Added", "value": "date-added", "type": "sort_by"},
            {"label": "Ascending", "value": "ascending", "type": "order"},
            {"label": "Descending", "value": "descending", "type": "order"},
        ]
        self.sorting_option_config = {"sort_by": "name", "order": "ascending"}
        for option in context_options:
            context_menu.add_command(
                label=option.get("label"), command=lambda option=option: self.perform_selected_option(option))
        for option in sorting_options:
            if option["value"] == "ascending":
                options_menu.add_separator()
            options_menu.add_command(
                label=option.get("label"), command=lambda option=option: self.perform_selected_sorting(option))

        def show_context_menu(event):
            context_menu.post(event.x_root, event.y_root)

        def show_sorting_menu(event):
            options_menu.post(event.x_root, event.y_root)

        self.add_button.bind("<Button-1>", show_context_menu)
        self.three_dots_button.bind("<Button-1>", show_sorting_menu)

        # pack the  right frame
        self.right_frame = tk.Frame(self, bg="white")
        self.right_frame.pack(side="right", fill="both", expand=True)

        self.folder_list = self.myvault.get_initials()
        self.icon_folder = tk.PhotoImage(
            file="resources/images/structure.png", width=150, height=150)
        self.icon_text_file = tk.PhotoImage(
            file="resources/images/text-file.png", width=150, height=150)
        self.icon_image = tk.PhotoImage(
            file="resources/images/image.png", width=150, height=150)
        self.icon_simple_file = tk.PhotoImage(
            file="resources/images/simple-file.png", width=150, height=150)
        self.render_listing(self.folder_list)

        self.current_active_directory = None
        self.current_selected_fileTree = None

        # WARNING: calling the mainloop method here is un-necessary and may cause unwanted behaviors
        # self.mainloop()

    def perform_selected_sorting(self, selected_option):
        if selected_option["type"] == "sort_by":
            self.sorting_option_config["sort_by"] = selected_option["value"]
        else:
            self.sorting_option_config["order"] = selected_option["value"]
        self.folder_list = list(self.folder_list)
        Sort(self.sorting_option_config).quick_sort(
            self.folder_list, 0, len(self.folder_list) - 1)
        self.render_listing(self.folder_list)

    def perform_selected_option(self, selected_option):
        if EncryptedFileTree.objects.filter(id=self.current_active_directory).exists():
            fileTree = EncryptedFileTree.objects.get(
                id=self.current_active_directory)
        else:
            fileTree = None
        if selected_option.get("value") == "create":
            value = simpledialog.askstring(
                "Input", "Enter the name for the folder:")
            if value:
                self.myvault.create_folder(value, fileTree)
        elif selected_option.get("value") == "add-file":
            file_path = filedialog.askopenfilename()
            # print(file_path)
            if file_path:
                self.myvault.insert_file(file_path, fileTree)
        elif selected_option.get("value") == "add-folder":
            folder_path = filedialog.askdirectory()
            # print(folder_path)
            if folder_path:
                folder_path += "/"
                self.myvault.insert_folder(folder_path, fileTree)
        self.refresh_active_content(self.current_active_directory)

    def show_about_us(self):
        self.right_frame.destroy()
        self.right_frame = tk.Frame(self, bg="white")
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.set_breadcrumb(data=[{
            "name": "About Us",
            "id": None,
        }])

        self.notebook = ttk.Notebook(self.right_frame, width=700, height=700)

        # create three tabs
        tab1 = ttk.Frame(self.notebook)
        tab2 = ttk.Frame(self.notebook)
        tab3 = ttk.Frame(self.notebook)
        tab4 = ttk.Frame(self.notebook)

        # add the tabs to the notebook
        self.notebook.add(tab1, text="Darpan Kattel")
        self.notebook.add(tab2, text="Bishnu Datt Badu")
        self.notebook.add(tab3, text="Bibek Sunar")
        self.notebook.add(tab4, text="Javed Ansari")

        # add some content to the tabs
        self.darpan = tk.Label(tab1, background="white")
        self.ppdarpan = tk.PhotoImage(
            file="resources/images/darpan-kattel.png")
        self.ppdarpan = self.ppdarpan.subsample(2, 2)
        self.photod = tk.Label(
            self.darpan, image=self.ppdarpan, background="white")
        self.photod.pack()
        self.text = tk.Label(self.darpan, text="Darpan kattel\n077BCT099", font=(
            "Arial", 20, "bold"), background="white").pack()
        self.text = tk.Button(
            self.darpan, text="linkedin.com/in/darpankattel/", font=("Arial", 15), background="white", foreground="blue", cursor="hand2", command=lambda: self.open_link("https://www.linkedin.com/in/darpankattel/"), bd=0).pack()
        self.darpan.pack()

        self.bishnu = tk.Label(tab2, background="white")
        self.ppbishnu = tk.PhotoImage(
            file="resources/images/bishnu.png")
        self.ppbishnu = self.ppbishnu.subsample(2, 2)
        self.photob = tk.Label(
            self.bishnu, image=self.ppbishnu, background="white")
        self.photob.pack()
        self.text = tk.Label(self.bishnu, text="Bishnu Datt Badu\n077BCT098", font=(
            "Arial", 20, "bold"), background="white").pack()
        self.text = tk.Button(
            self.bishnu, text="facebook.com/bishnudbadu.143", font=("Arial", 15), background="white", foreground="blue", cursor="hand2", command=lambda: self.open_link("https://www.facebook.com/bishnudbadu.143"), bd=0).pack()
        self.bishnu.pack()

        self.bibek = tk.Label(tab3, background="white")
        self.ppbibek = tk.PhotoImage(file="resources/images/bibek-sunar.png")
        self.ppbibek = self.ppbibek.subsample(2, 2)
        self.photov = tk.Label(
            self.bibek, image=self.ppbibek, background="white")
        self.photov.pack()
        self.text = tk.Label(self.bibek, text="Bibek Sunar\n 077BCT097", font=(
            "Arial", 20, "bold"), background="white").pack()
        self.text = tk.Button(
            self.bibek, text="linkedin.com/in/darpankattel/", font=("Arial", 15), background="white", foreground="blue", cursor="hand2", command=lambda: self.open_link("https://www.linkedin.com/in/darpankattel/"), bd=0).pack()
        self.bibek.pack()

        self.javed = tk.Label(tab4, background="white")
        self.ppjaved = tk.PhotoImage(file="resources/images/javed-ansari.png")
        self.ppjaved = self.ppjaved.subsample(2, 2)
        self.photoj = tk.Label(
            self.javed, image=self.ppjaved, background="white")
        self.photoj.pack()
        self.text = tk.Label(self.javed, text="Javed Ansari\n077BCT033", font=(
            "Arial", 20, "bold"), background="white").pack()
        self.text = tk.Button(
            self.javed, text="linkedin.com/in/darpankattel/", font=("Arial", 15), background="white", foreground="blue", cursor="hand2", command=lambda: self.open_link("https://www.linkedin.com/in/darpankattel/"), bd=0).pack()
        self.javed.pack()
        self.notebook.pack()

    def get_content(self, fileTreeId=None):
        if not fileTreeId:
            self.folder_list = self.myvault.get_initials()
        else:
            self.folder_list = self.myvault.get_children(fileTreeId)
        return self.folder_list

    def get_voice(self):
        self.folder_list = self.myvault.get_voice()
        return self.folder_list

    def get_video(self):
        self.folder_list = self.myvault.get_video()
        return self.folder_list

    def get_picture(self):
        self.folder_list = self.myvault.get_picture()
        return self.folder_list

    def get_document(self):
        self.folder_list = self.myvault.get_document()
        return self.folder_list

    def logout(self):
        confirmed = messagebox.askyesnocancel(
            "Logout?", "Are you sure to logout?")
        if confirmed:
            self.auth.logout()
            self.destroy()

    def refresh_active_content(self, id):
        data = self.get_content(id)
        self.render_listing(data)
        self.set_breadcrumb(id)
        self.current_active_directory = id
        self.current_selected_fileTree = None

    def handle_double_click(self, id):
        if not self.myvault.is_file(id):
            data = self.get_content(id)
            self.render_listing(data)
            self.set_breadcrumb(id)
            self.current_active_directory = id
            self.current_selected_fileTree = None
        else:
            self.current_selected_fileTree = id
            file = self.myvault.get_encrypted_file_tree(id)
            file_extension = get_file_extension(file.name)
            if file_extension in ["rtf", "doc", "docx", "wps", "wpd", "odt"]:
                self.display_rich_text_file(id)
            elif file_extension == "txt":
                self.display_text_file(id)
            elif file_extension in ["jpg", "jpeg", "png"]:
                self.display_image(id)
            else:
                messagebox.showinfo(
                    "Unknown File Format", "This file format isn't supported. Kindly export and view it.")

    def perform_selected_context_option(self, option, id, ask_prompt=True):
        if option.get("value") == "export":
            folder_path = filedialog.askdirectory()
            if folder_path:
                folder_path += "/"
                self.myvault.export(
                    self.myvault.get_encrypted_file_tree(id), folder_path)
                self.perform_selected_context_option(
                    {"value": "delete", "label": "delete"}, id, False)
                messagebox.showinfo(
                    "Exported", f"Your file/folder has been exported to {folder_path}")
        elif option.get("value") == "delete":
            if ask_prompt:
                confirmed = messagebox.askyesnocancel(
                    "Delete?", "Are you sure to delete?")
            else:
                confirmed = True
            if confirmed:
                try:
                    self.myvault.delete_fileTree(id)
                    self.refresh_active_content(self.current_active_directory)
                except FileNotFoundError:
                    messagebox.showwarning(
                        "Coudln't delete", "Couldn't delete the file/folder. Perhaps it doesn't exist.")
        else:
            print("Unknown")

    def handle_right_click(self, event, id):
        context_menu = tk.Menu(self.master, tearoff=0)
        options = [
            {"label": "Export", "value": "export"},
            {"label": "Delete", "value": "delete"},
            {"label": "Rename", "value": "Rename"}
        ]
        for option in options:
            context_menu.add_command(
                label=option.get("label"), command=lambda option=option: self.perform_selected_context_option(option, id))
        context_menu.post(event.x_root, event.y_root)

    def display_text_file(self, id):
        try:
            self.text_window = tk.Toplevel(self.master, width=900, height=800)
            self.text_window.minsize(700, 600)
            self.text_window.iconbitmap("resources/images/icon.ico")
            text_widget = tk.Text(
                self.text_window, wrap='word', height=20, width=80)
            text_widget.insert('1.0', self.myvault.get_decrypted(
                EncryptedFileTree.objects.get(id=id)))
            text_widget.pack(fill='both', expand=True)
            self.text_window.focus_force()
        except FileNotFoundError:
            self.text_window.destroy()
            messagebox.showerror("File Not Found", "The file wasn't found.")

    def display_rich_text_file(self, id):
        try:
            self.rich_text_window = tk.Toplevel(
                self.master, width=900, height=800)
            self.rich_text_window.minsize(700, 600)
            self.rich_text_window.iconbitmap("resources/images/icon.ico")

            text_widget = scrolledtext.ScrolledText(
                self.rich_text_window)
            text_widget.pack(fill="both")

            # rtf_text = '{\\rtf1\\ansi\\ansicpg1252\\deff0\\deflang1033{\\fonttbl{\\f0\\fnil\\fcharset0 Arial;}}\n\\viewkind4\\uc1\\pard\\f0\\fs20 This is some RTF formatted text.\\par}\n'
            text_widget.insert('1.0', self.myvault.get_decrypted(
                EncryptedFileTree.objects.get(id=id)))
            self.rich_text_window.focus_force()
        except FileNotFoundError:
            self.rich_text_window.destroy()
            messagebox.showerror("File Not Found", "The file wasn't found.")

    def display_image(self, id):
        self.image_view_window = tk.Toplevel(
            self.master, width=900, height=800)
        self.image_view_window.minsize(700, 600)
        self.image_view_window.iconbitmap("resources/images/icon.ico")

        temp_path = self.myvault.export_temp(
            self.myvault.get_encrypted_file_tree(id))

        # Open the image using PIL
        pil_image = Image.open(temp_path)

        # Create a PhotoImage object from the PIL image
        self.temp__photo = ImageTk.PhotoImage(pil_image)
        label = tk.Label(self.image_view_window,
                         image=self.temp__photo, background="white")

        # Set the size of the label to the size of the image
        label.config(width=self.temp__photo.width(),
                     height=self.temp__photo.height())

        # Place the label at (0, 0) and make it fill the entire space of the toplevel window
        label.place(x=0, y=0, relwidth=1, relheight=1)

        self.image_view_window.focus_force()

    def render_listing(self, folder_list):
        def create_double_click_handler(element):
            def double_click_handler(event=None):
                self.handle_double_click(element.id)
            return double_click_handler

        def create_right_click_handler(element):
            def right_click_handler(event=None):
                self.handle_right_click(event, element.id)
            return right_click_handler
        for elem in self.right_frame.winfo_children():
            elem.destroy()

        for i, element in enumerate(folder_list):
            file_extension = get_file_extension(element.name)
            if element.is_directory:
                icon = self.icon_folder
            elif file_extension == "txt":
                icon = self.icon_text_file
            elif file_extension in ["jpg", "jpeg", "png"]:
                icon = self.icon_image
            else:
                icon = self.icon_simple_file
            icon_btn = tk.Button(self.right_frame, image=icon,
                                 bd=0, activebackground="white", bg="white", cursor="hand2")
            icon_btn.grid(row=1, column=i)
            icon_btn.bind('<Double-Button-1>',
                          create_double_click_handler(element))
            icon_btn.bind('<Button-3>',
                          create_right_click_handler(element))
            element_name = element.name
            if len(element_name) > 15:
                element_name = element_name[:15] + "..."
            name = tk.Label(self.right_frame, text=element_name, font=(
                "Arial", 12, "bold"), bg="white")
            name.grid(row=2, column=i)
        if len(folder_list) == 0:
            self.status_label = tk.Label(
                self.right_frame, text="Nothing resides here...", font=(
                    "Arial", 15), foreground="red", background="white", padx=10)
            self.status_label.grid(row=0, column=0)

    def set_home(self):
        self.render_listing(self.get_content())
        self.set_breadcrumb()
        self.current_active_directory = None
        self.current_selected_fileTree = None

    def set_voice(self):
        self.render_listing(self.get_voice())
        self.set_breadcrumb(data=[{
            "name": "Voice",
            "id": None,
        }])
        self.current_active_directory = None
        self.current_selected_fileTree = None

    def set_video(self):
        self.render_listing(self.get_video())
        self.set_breadcrumb(data=[{
            "name": "Videos",
            "id": None,
        }])
        self.current_active_directory = None
        self.current_selected_fileTree = None

    def set_picture(self):
        self.render_listing(self.get_picture())
        self.set_breadcrumb(data=[{
            "name": "Picture",
            "id": None,
        }])
        self.current_active_directory = None
        self.current_selected_fileTree = None

    def set_document(self):
        self.render_listing(self.get_document())
        self.set_breadcrumb(data=[{
            "name": "Docs",
            "id": None,
        }])
        self.current_active_directory = None
        self.current_selected_fileTree = None

    def set_breadcrumb(self, id=None, data=None):
        if not data:
            if id:
                self.breadcrumb_list = [{
                    "name": "Home",
                    "id": None,
                }] + EncryptedFileTree.objects.get(
                    id=id).get_relative_list()
            else:
                self.breadcrumb_list = [{
                    "name": "Home",
                    "id": None,
                }]
        else:
            self.breadcrumb_list = data
        self.render_breadcrumb()

    def render_breadcrumb(self):
        def navigate_from_breadcrumb(element):
            def double_click_handler(event=None):
                if element.get("id"):
                    self.handle_double_click(element.get("id"))
                else:
                    self.set_home()
            return double_click_handler
        for elem in self.breadcrumb.winfo_children():
            elem.destroy()
        for i, elem in enumerate(self.breadcrumb_list):
            label = tk.Button(self.breadcrumb, text=elem.get("name"), font=(
                "Arial", 10, "bold"), bg="white", cursor="hand2", bd=0, activebackground="white", command=navigate_from_breadcrumb(elem))
            label.grid(row=0, column=i*2+1, sticky="w")
            if i != len(self.breadcrumb_list) - 1:
                separator = tk.Label(self.breadcrumb, text=">", font=(
                    "Arial", 10, "bold"), bg="white")
                separator.grid(row=0, column=i*2+2, sticky="e")

    def ask_tour_and_directory(self):
        def ask_directory():
            folder_path = filedialog.askdirectory()
            if folder_path:
                folder_path += "/"
                if self.myvault.set_storage_location(folder_path):
                    messagebox.showinfo("Success",
                                        f"Default storage location set to {folder_path}")
                    self.touring_window.destroy()
                    self.deiconify()
        self.withdraw()

        self.touring_window = tk.Toplevel(self)
        self.touring_window.configure(bg="#C399CC")

        self.wright_frame = tk.Frame(self.touring_window, bg="#C399CC")
        self.wright_frame.pack(side="right", fill="y")

        self.logo_frame = tk.Frame(self.wright_frame, bg="#C399CC")
        self.logo_frame.grid(row=2, column=2, sticky="n", pady=80)

        self.original_image_main = Image.open("resources/images/main_logo.png")
        self.resized_image_main = self.original_image_main.resize(
            (int(self.original_image_main.width * 0.75), int(self.original_image_main.height * 0.75)))
        self.main = ImageTk.PhotoImage(self.resized_image_main)
        self.wel_ri_label2 = tk.Label(
            self.logo_frame, image=self.main, bg="#C399CC")
        # store a reference to the image to avoid garbage collection
        self.wel_ri_label2.image = self.main
        self.wel_ri_label2.pack(side="left", padx=(0, 20))

        self.wel_ri_crypt = tk.Label(self.logo_frame, text="CRYPT", font=(
            "Arial", 20, "bold"), bg="#C399CC", fg="black")
        self.wel_ri_crypt.pack(side="right")

        self.wel_ri_text = tk.Label(self.wright_frame, text="NEXT:\nWe will ask you a directory\n to save all encrypted data.", font=(
            "Arial", 20), bg="#C399CC", fg="black")
        self.wel_ri_text.grid(row=3, column=2)

        self.man = tk.PhotoImage(file="resources/images/man.png")
        self.wel_label1 = tk.Label(
            self.wright_frame, image=self.man, bg="#C399CC")
        self.wel_label1.grid(row=2, column=3, sticky="se", pady=120, rowspan=8)

        self.original_image = Image.open("resources/images/get_started.png")
        self.resized_image = self.original_image.resize(
            (int(self.original_image.width * 0.75), int(self.original_image.height * 0.75)))
        self.get_started_button_photo = ImageTk.PhotoImage(self.resized_image)
        self.get_started_button = tk.Button(self.wright_frame, image=self.get_started_button_photo, bg="#C399CC", fg="#862d86", font=(
            "Arial", 20), bd=0, activebackground="#C399CC", activeforeground="#862d86", cursor="hand2", width=400, command=ask_directory)
        self.get_started_button.grid(row=4, column=2, padx=(10, 0))

        self.wleft_frame = tk.Frame(self.touring_window, bg="#C399CC")
        self.wleft_frame.pack(side="left", fill="y")

        self.le_frame1 = tk.Frame(self.wleft_frame, bg="#C399CC")
        self.le_frame1.grid(row=0, column=0, pady=40, padx=40, ipadx=40)

        self.wel_le_text1 = tk.Label(self.le_frame1, text="Are you ready to safe your", font=(
            "Arial", 30), bg="#C399CC", fg="black")
        self.wel_le_text1.grid(row=0, column=0, sticky="w")

        self.wel_le_text1 = tk.Label(self.le_frame1, text="personal data's?", font=(
            "Arial", 30), bg="#C399CC", fg="black")
        self.wel_le_text1.grid(row=1, column=0, sticky="w")

        self.original_image_pic = Image.open("resources/images/pic.png")
        self.resized_image_pic = self.original_image_pic.resize(
            (int(self.original_image_pic.width * 0.75), int(self.original_image_pic.height * 0.75)))
        self.main_pic = ImageTk.PhotoImage(self.resized_image_pic)
        self.wel_le_label1 = tk.Label(
            self.le_frame1, image=self.main_pic, bg="#C399CC")
        self.wel_le_label1.grid(row=2, column=0, sticky="w", pady=10)

        self.original_image_voi = Image.open("resources/images/voi.png")
        self.resized_image_voi = self.original_image_voi.resize(
            (int(self.original_image_voi.width * 0.75), int(self.original_image_voi.height * 0.75)))
        self.main_voi = ImageTk.PhotoImage(self.resized_image_voi)
        self.wel_le_label1 = tk.Label(
            self.le_frame1, image=self.main_voi, bg="#C399CC")
        self.wel_le_label1.grid(row=3, column=0, sticky="w", pady=10)

        self.original_image_vid = Image.open("resources/images/vid.png")
        self.resized_image_vid = self.original_image_vid.resize(
            (int(self.original_image_vid.width * 0.75), int(self.original_image_vid.height * 0.75)))
        self.main_vid = ImageTk.PhotoImage(self.resized_image_vid)
        self.wel_le_label1 = tk.Label(
            self.le_frame1, image=self.main_vid, bg="#C399CC")
        self.wel_le_label1.grid(row=4, column=0, sticky="w", pady=10)

        self.original_image_doc = Image.open("resources/images/doc.png")
        self.resized_image_doc = self.original_image_doc.resize(
            (int(self.original_image_doc.width * 0.75), int(self.original_image_doc.height * 0.75)))
        self.main_doc = ImageTk.PhotoImage(self.resized_image_doc)
        self.wel_le_label1 = tk.Label(
            self.le_frame1, image=self.main_doc, bg="#C399CC")
        self.wel_le_label1.grid(row=5, column=0, sticky="w", pady=10)

        self.le_frame2 = tk.Frame(self.wleft_frame, bg="#C399CC")
        self.le_frame2.grid(row=3, column=0, sticky="s", pady=40, padx=40)

        self.wel_le_text3 = tk.Label(self.le_frame2, text="CRYPT", font=(
            "Arial", 25, "bold", "underline"), bg="#C399CC", fg="black")
        self.wel_le_text3.grid(row=0, column=0, sticky="w")

        self.wel_le_text4 = tk.Label(self.le_frame2, text="We save your data very safely and we", font=(
            "Arial", 25), bg="#C399CC", fg="black")
        self.wel_le_text4.grid(row=1, column=0, sticky="w")

        self.wel_le_text5 = tk.Label(self.le_frame2, text="give some extra memory for storing", font=(
            "Arial", 25), bg="#C399CC", fg="black")
        self.wel_le_text5.grid(row=2, column=0, sticky="w")

        self.wel_le_text6 = tk.Label(self.le_frame2, text="your private data.", font=(
            "Arial", 25), bg="#C399CC", fg="black")
        self.wel_le_text6.grid(row=3, column=0, sticky="w")

        self.canvas = tk.Canvas(self.touring_window,
                                width=2, height=self.winfo_height())
        self.canvas.create_line(0, 0, 0, self.winfo_height(), fill="black")
        self.canvas.pack(side="left", fill="y")
        # self.canvas.pack(side="right", fill="y")

    def show_profile(self):
        for elem in self.right_frame.winfo_children():
            elem.destroy()
        self.right_frame.config(bg="#ffffff")

        current_user = self.auth.get_current_user()

        # Display user information in the window
        self.photo = tk.PhotoImage(file="resources/images/userphoto.png")
        self.label = tk.Label(self.right_frame, image=self.photo, bg="#ffffff")
        self.label.grid(row=0, column=0, sticky="w")

        self.user_info_frame = tk.Frame(self.right_frame, bg="#ffffff")
        self.user_info_frame.grid(row=0, column=1, sticky="w")

        self.user_info_label = tk.Label(self.user_info_frame, text="Personal information", font=(
            "Arial", 30, "bold", "underline"), bg="#ffffff")
        self.user_info_label.grid(row=0, column=0, pady=10, columnspan=3)

        self.user_info_label = tk.Label(
            self.user_info_frame, text=f"Last Login: {get_formatted_date(current_user.user.last_login)}", font=("Arial", 15), bg="#ffffff")
        self.user_info_label.grid(row=1, column=0, sticky="w")

        self.user_info_label = tk.Label(
            self.user_info_frame, text=f"Date Joined: {get_formatted_date(current_user.user.date_joined)}", font=("Arial", 15), bg="#ffffff")
        self.user_info_label.grid(row=2, column=0)

        self.user_detail = tk.Frame(self.right_frame, bg="#ffffff")
        self.user_detail.grid(row=2, column=1)

        self.user_info_label4 = tk.Label(
            self.user_detail, text=f"Name: {current_user.full_name}", font=("Arial", 18), bg="#ffffff")
        self.user_info_label4.grid(row=0, column=0, pady=10, sticky="w")
        self.user_info_label1 = tk.Label(
            self.user_detail, text=f"Username: {current_user.user.username}", font=("Arial", 18), bg="#ffffff")
        self.user_info_label1.grid(row=1, column=0, pady=10, sticky="w")
        self.user_info_label2 = tk.Label(
            self.user_detail, text=f"Email: {current_user.user.email}", font=("Arial", 18), bg="#ffffff")
        self.user_info_label2.grid(row=2, column=0, pady=10, sticky="w")
        self.user_info_label3 = tk.Label(
            self.user_detail, text=f"Def. Storage Directory: {current_user.directory}", font=("Arial", 18), bg="#ffffff")
        self.user_info_label3.grid(row=3, column=0, pady=10, sticky="w")
        # self.user_info_label4 = tk.Label(
        #     self.user_detail, text="Email: 077bct099.darpan@pcampus.edu.np", font=("Arial", 18), bg="#ffffff")
        # self.user_info_label4.grid(row=4, column=0, pady=10, sticky="w")
        # self.user_info_label5 = tk.Label(
        #     self.user_detail, text="Folder Directory: C:/Users/OneDrive/Documents", font=("Arial", 18), bg="#ffffff")
        # self.user_info_label5.grid(row=5, column=0, pady=10, sticky="w")
        # self.user_info_label6 = tk.Label(
        #     self.user_detail, text="Email: 077bct099.darpan@pcampus.edu.np", font=("Arial", 18), bg="#ffffff")
        # self.user_info_label6.grid(row=6, column=0, pady=10, sticky="w")
        # self.user_info_label7 = tk.Label(
        #     self.user_detail, text="Folder Directory: C:/Users/OneDrive/Documents", font=("Arial", 18), bg="#ffffff")
        # self.user_info_label7.grid(row=7, column=0, pady=10, sticky="w")

    def open_link(self, link):
        webbrowser.open_new_tab(link)
