#  home_screen.py
#  Created by Yaagyanika Gehlot on 28/12/25.

# Imports
from PIL import Image
import customtkinter as ctk

# User Imports
from constants import *
from utils import *

class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=OUTER_BG)
        self.grid_columnconfigure(0, weight=1)

        # Title
        title_image = create_pixel_text_image(PIXEL_TITLE, OUTER_BG, text_color="black", font_size=42, img_size=(220, 60))
        title_label = ctk.CTkLabel(self, image=title_image, text="")
        title_label.grid(row=0, column=0, columnspan=3, sticky="w")

        # Inner box
        inner_box = ctk.CTkFrame(self, fg_color=INNER_BOX_BG, corner_radius=10)
        inner_box.grid(row=1, column=0, sticky="nsew", padx=10)
        inner_box.grid_columnconfigure((0,1), weight=1)

        # Home Page text in Pixel
        home_text = create_pixel_text_image(HOME_PAGE, INNER_BOX_BG, text_color="black", font_size=32, img_size=(220,120))
        home_label = ctk.CTkLabel(inner_box, image=home_text, text="")
        home_label.grid(row=0, column=0, columnspan=2, padx=(20,0), pady=10, sticky="w")

        # Chef image
        remy_img = ctk.CTkImage(light_image=Image.open(CHEF_IMG_PATH), size=(170,200))
        remy_label = ctk.CTkLabel(inner_box, image=remy_img, text="")
        remy_label.grid(row=1, column=1, sticky="se", padx=10, pady=10)

        # Start button text in Pixel
        start_text = create_pixel_text_image("Start", INNER_BOX_BG, text_color=START_BTN_COLOR, font_size=600, img_size=(150,40), bg_image_path=BORDER_IMG_PATH)
        # Create a button using that image
        start_button = ctk.CTkButton(inner_box, image=start_text, text="", fg_color=INNER_BOX_BG, hover_color=INNER_BOX_BG, border_width=0,
                                   command=lambda: print("Start pressed!"))
        start_button.grid(row=2, column=0, columnspan=2, padx=0, pady=(0,10))