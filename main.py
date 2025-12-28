#  main.py
#  Created by Yaagyanika Gehlot on 21/12/25.

# Imports
import os
import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw, ImageFont

# User Imports
from constants import *

# Variables


class EggTimer:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.configure(fg_color=OUTER_BG)
        self.root.geometry("350x520")

        # Outer Yellow Border
        outer_frame = ctk.CTkFrame(self.root, fg_color=OUTER_BG)
        outer_frame.grid(row=0, column=0, padx=10, sticky = 'nsew')

        # Title Name with Pixel Font 
        title_image = create_pixel_text_image(PIXEL_TITLE, OUTER_BG, font_size=42, img_size=(220,60))
        # Add to Label 
        title_label = ctk.CTkLabel(outer_frame, image=title_image, text="") 
        title_label.grid(row=0, column=0, sticky='w')

        # Internal Light Yellow Background Box
        inner_box = ctk.CTkFrame(outer_frame, fg_color=INNER_BOX_BG, corner_radius=10)
        inner_box.grid(row=1, column=0, columnspan=3, rowspan=2, padx=10) 

        # Home Page Text with Pixel Font 
        home_text = create_pixel_text_image(HOME_PAGE, INNER_BOX_BG, font_size=32, img_size=(220,200))
        # Add to Label 
        home_label = ctk.CTkLabel(inner_box, width=290, height=40, image=home_text, text="") 
        home_label.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky='w')

        # Pixel Remy image inside the inner box
        remy_img = ctk.CTkImage(light_image=Image.open(CHEF_IMG_PATH), size=(200, 200))
        remy_label = ctk.CTkLabel(inner_box, image=remy_img, text="")
        remy_label.grid(row=2, column=2, padx=(0,10), pady=(0,10), sticky="e")

def create_pixel_text_image(text, bg_color, font_size, img_size):
    # Define the path to the font file 
    font_path = os.path.join(LIB_FONT_PATH, "PixelifySans-Regular.ttf") 
    
    # Create a blank image with Yellow background with drawing context 
    image = Image.new('RGB', size=img_size, color=bg_color) 
    draw = ImageDraw.Draw(image) 
    
    # Load the pixel font and specify size 
    try: 
        font = ImageFont.truetype(font_path, font_size)
    except IOError: 
        print(f"Error: Font file not found at {font_path}. Using default font.") 
        font = ImageFont.load_default() 
    
    # Add text using the custom font and save the image 
    draw.text(xy=(5,5), text=text, fill="black", font=font) 

    # Uncomment below lines to save the image to check size properly
    # output_path = os.path.join(LIB_IMG_PATH, "pixelify_sans_text.png") 
    # image.save(output_path)
    # image.show()
    
    # Convert PIL Image 
    title_image = ctk.CTkImage(light_image=image,size=img_size) 
    
    # Convert to CTkImage
    return title_image

if __name__ == "__main__":
    root = ctk.CTk()
    app = EggTimer(root)

    # TODO: Quick app close for debugging. Remove 76-77 later
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()
