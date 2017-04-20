import tkinter as tk
import tkinter.messagebox
import glob
import os

import sys
from PIL import ImageTk, Image, ImageFilter

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
        
    def get_current_image(self):
        selected_index = self.shown_image_index % len(self.all_image_paths)
        selected_image_path = self.all_image_paths[selected_index]
        
        return Image.open(selected_image_path)
    
    # Saves the currently viewed image under the "saved-image" name.
    def on_save_click(self, root_window):
        self.get_current_image().save("saved-image.jpg", "JPEG")
        
    # Displays the next image in the folder.
    def on_next_button_click(self):
        self.shown_image_index += 1
        self.change_image(self.shown_image_index)

    # Displays the previous image in the folder.
    def on_prev_button_click(self):
        self.shown_image_index -= 1
        self.change_image(self.shown_image_index)
    
    # Refreshes the currently viewed image by switching it for a new one.
    def refresh_image_label(self, new_image):
        self.panel.configure(image = new_image)
        self.panel.new_image = new_image
        
    # Applies a filtered version of the image to its label.
    def filter_image(self, image_filter):
        self.panel.photograph = self.get_current_image()
        
        filtered_pill_image = self.panel.photograph.filter(image_filter)
        filtered_tk_image = ImageTk.PhotoImage(filtered_pill_image)
        
        self.refresh_image_label(filtered_tk_image)
    
    # Changes the label image so that is matches the current user choice.
    def change_image(self, new_image_index):
        pill_image = self.get_current_image()
        tk_image = ImageTk.PhotoImage(pill_image)
        
        self.refresh_image_label(tk_image)
        
    def setup_menubar(self, window):
        menu_bar = tk.Menu(window)

        # Define the "File" menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save",
                command=lambda: self.on_save_click(window))
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=window.quit)

        # Append the file menu to the menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Define the "Filter" menu
        filter_menu = tk.Menu(menu_bar, tearoff=0)
        filter_menu.add_command(label="Normal",
                command=lambda: self.change_image(self.shown_image_index))
        filter_menu.add_command(label="Blur",
                command=lambda: self.filter_image(ImageFilter.BLUR))
        filter_menu.add_command(label="Contour",
                command=lambda: self.filter_image(ImageFilter.CONTOUR))
        filter_menu.add_command(label="Detail",
                command=lambda: self.filter_image(ImageFilter.DETAIL))
        filter_menu.add_command(label="Enhance edge",
                command=lambda: self.filter_image(ImageFilter.EDGE_ENHANCE))
        filter_menu.add_command(label="Enhance edge more",
                command=lambda: self.filter_image(ImageFilter.EDGE_ENHANCE_MORE))
        filter_menu.add_command(label="Emboss",
                command=lambda: self.filter_image(ImageFilter.EMBOSS))
        filter_menu.add_command(label="Find edges",
                command=lambda: self.filter_image(ImageFilter.FIND_EDGES))
        filter_menu.add_command(label="Smooth",
                command=lambda: self.filter_image(ImageFilter.SMOOTH))
        filter_menu.add_command(label="Smooth more",
                command=lambda: self.filter_image(ImageFilter.SMOOTH_MORE))
        filter_menu.add_command(label="Sharpen",
                command=lambda: self.filter_image(ImageFilter.SHARPEN))

        # Append the filter menu to the menu bar
        menu_bar.add_cascade(label="Filter", menu=filter_menu)

        # Define the "Help" menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About",
                command=lambda: self.show_about_window(window))

        # Append the help menu to the menu bar
        menu_bar.add_cascade(label="Help", menu=help_menu)

        window.config(menu=menu_bar)

    def start(self):
        # Data
        
        self.all_image_paths = glob.glob(os.getcwd() + "\*.jpg")
        self.shown_image_index = 0
        
        # User interface
        gallery_window = GalleryWindow()
        gallery_window.window.title("Advanced Photo Viewer")
        gallery_window.window.configure(background='white')
        gallery_window.window.protocol(
                "WM_DELETE_WINDOW",
                lambda: gallery_window.ensure_app_exit())

        # Window icon
        icon = tk.PhotoImage(file='icon.gif')
        gallery_window.window.call('wm', 'iconphoto', gallery_window.window._w, icon)

        prev_button = tk.Button(
            gallery_window.window,
            text="Prev",
            command=lambda: self.on_prev_button_click(),
            bg="lightblue",
            relief=tk.FLAT)
        prev_button.pack(padx=250, pady=10, side=tk.LEFT)

        # Image related stuff
        path = self.all_image_paths[self.shown_image_index]

        # Creates a Tkinter-compatible photo image, which can be used everywhere
        # Tkinter expects an image object.
        image = ImageTk.PhotoImage(Image.open(path))

        # The Label widget is a standard Tkinter widget used to display a
        # text or image on the screen.
        self.panel = tk.Label(gallery_window.window, image = image)
        self.panel.photograph = Image.open(path)
        self.panel.pack(padx=5, pady=20, side=tk.LEFT)

        next_button = tk.Button(
                gallery_window.window,
                text="Next",
                command=lambda: self.on_next_button_click(),
                bg="lightblue",
                relief=tk.FLAT)
        next_button.pack(padx=250, pady=20, side=tk.LEFT)

        self.setup_menubar(gallery_window.window)

        gallery_window.window.mainloop()

class GalleryWindow:

    def __init__(self):
        self.window = tk.Tk()
        #self.window.attributes('-zoomed', True)
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

    def ensure_app_exit(self):
        if tkinter.messagebox.askyesno('Question', 'Are you sure you want to exit the viewer?'):
            sys.exit()

if __name__ == '__main__':
    s = Startup()
    s.start()
