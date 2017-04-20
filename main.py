import tkinter as tk
import sys
from PIL import ImageTk, Image

class Startup:
    def show_about_window(self, root_window):
        about_window = tk.Toplevel(root_window)
        about_window.wm_title("Help")
        description_label = tk.Label(
                about_window,
                text="This is a project for the computer graphics class in TUES.")
        description_label.pack(padx=30, pady=10)

        credit_label = tk.Label(
                about_window,
                text="Made by Nikolay Karagyozov, Ivaylo Arnaudov and Toma Marinov.")
        credit_label.pack(padx=30, pady=10)

    def on_button_click(self):
        pass

    def setup_menubar(self, window):
        menu_bar = tk.Menu(window)

        # Define the "File" menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open",
                command=lambda: self.on_button_click(window))
        file_menu.add_command(label="Save",
                command=lambda: self.on_button_click(window))
        file_menu.add_command(label="Close",
                command=lambda: self.on_button_click(window))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)

        # Append the file menu to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Define the "Filter" menu
        filter_menu = tk.Menu(menu_bar, tearoff=0)
        filter_menu.add_command(label="Negative",
                command=lambda: self.on_button_click(window))
        filter_menu.add_command(label="Gaussian blur",
                command=lambda: self.on_button_click(window))

        # Append the filter menu to the menu bar
        menu_bar.add_cascade(label="Filter", menu=filter_menu)

        # Define the "Help" menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About",
                command=lambda: self.show_about_window(window))

        # Append the help menu to the menu bar
        menu_bar.add_cascade(label="Help", menu=help_menu)

        window.config(menu=menu_bar)

    def next_image(self):

    def prev_image(self):

    def start(self):
        gallery_window = GalleryWindow()
        gallery_window.window.title("Advanced Photo Viewer")
        gallery_window.window.configure(background='white')

        icon = tk.PhotoImage(file='icon.gif')
        gallery_window.window.call('wm', 'iconphoto', gallery_window.window._w, icon)

        path = 'meme.jpg'

        # Creates a Tkinter-compatible photo image, which can be used everywhere
        # Tkinter expects an image object.
        image = ImageTk.PhotoImage(Image.open(path))

        prev_button = tk.Button(gallery_window.window, text="Prev", fg="red",
                command=self.prev_image)

        next_button = tk.Button(gallery_window.window, text="Next", fg="red",
                command=self.next_image)

        # The Label widget is a standard Tkinter widget used to display a
        # text or image on the screen.
        panel = tk.Label(gallery_window.window, image = image)

        # The Pack geometry manager packs widgets in rows or columns.
        panel.pack(side = "bottom", fill = "both", expand = "yes")

        self.setup_menubar(gallery_window.window)

        gallery_window.window.mainloop()

class GalleryWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-zoomed', True)
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.state = False
        self.window.bind("<F11>", self.toggle_fullscreen)
        self.window.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.window.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.window.attributes("-fullscreen", False)
        return "break"

if __name__ == '__main__':
    s = Startup()
    s.start()
