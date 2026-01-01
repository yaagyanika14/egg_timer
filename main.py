#  main.py
#  Created by Yaagyanika Gehlot on 21/12/25.

# Imports
import customtkinter as ctk

# User Imports
from constants import *
from screens.home_screen import HomeScreen

class EggTimer:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.configure(fg_color=OUTER_BG)
        self.root.geometry("350x520")
        self.root.grid_columnconfigure(0, weight=1)

        self.home_screen = HomeScreen(self.root)
        self.home_screen.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

if __name__ == "__main__":
    root = ctk.CTk()
    app = EggTimer(root)

    # TODO: Quick app close for debugging. Remove 76-77 later
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()
