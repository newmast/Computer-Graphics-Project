import tkinter as tk
import sys
from PIL import ImageTk, Image

class Startup:

    def on_button_click(self, root_window):
      file_win = tk.Toplevel(root_window)
      button = tk.Button(file_win, text="Do nothing button")
      button.pack()

    def setup_menubar(self, window):
        menu_bar = tk.Menu(window)

        # Define the "File" menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.on_button_click)
        file_menu.add_command(label="Open", command=self.on_button_click)
        file_menu.add_command(label="Save", command=self.on_button_click)
        file_menu.add_command(label="Save as...", command=self.on_button_click)
        file_menu.add_command(label="Close", command=self.on_button_click)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)

        # Append the file menu to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Define the "Edit" menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.on_button_click)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.on_button_click)
        edit_menu.add_command(label="Copy", command=self.on_button_click)
        edit_menu.add_command(label="Paste", command=self.on_button_click)
        edit_menu.add_command(label="Delete", command=self.on_button_click)
        edit_menu.add_command(label="Select All", command=self.on_button_click)

        # Append the edit menu to the menu bar
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Define the "Help" menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help Index", command=self.on_button_click)
        help_menu.add_command(label="About...", command=self.on_button_click)

        # Append the help menu to the menu bar
        menu_bar.add_cascade(label="Help", menu=help_menu)

        window.config(menu=menu_bar)

    def start(self):
        gallery_window = GalleryWindow()
        gallery_window.window.title("Advanced Photo Viewer")
        gallery_window.window.configure(background='white')

        path = 'meme.jpg'

        # Creates a Tkinter-compatible photo image, which can be used everywhere
        # Tkinter expects an image object.
        image = ImageTk.PhotoImage(Image.open(path))

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
