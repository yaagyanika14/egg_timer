#  utils.py
#  Created by Yaagyanika Gehlot on 28/12/25.

# Imports
import os
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont, ImageOps

# User Imports
from constants import *

def create_pixel_text_image(text, bg_color, text_color, font_size, img_size, bg_image_path=None):
    # Define the path to the font file 
    font_path = os.path.join(LIB_FONT_PATH, "PixelifySans-Regular.ttf") 
    
    # Create a blank image with Yellow background with drawing context
    if bg_image_path:
        image = Image.open(bg_image_path).convert("RGBA")
    else:    
        image = Image.new('RGB', size=img_size, color=bg_color) 
    
    img_w, img_h = image.size
    draw = ImageDraw.Draw(image) 
    
    # Load the pixel font and specify size 
    try: 
        font = ImageFont.truetype(font_path, font_size)
    except IOError: 
        print(f"Error: Font file not found at {font_path}. Using default font.") 
        font = ImageFont.load_default() 
    
    # Get text bounding box
    if "\n" in text:
        bbox = draw.multiline_textbbox((0, 0), text, font=font, spacing=2)
    else:
        bbox = draw.textbbox((0, 0), text, font=font)

    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Font metrics (ascent/descent)
    ascent, descent = font.getmetrics()
    # total height according to font
    font_height = ascent + descent

    # Center text vertically
    x = (img_w - text_w) // 2
    y = (img_h - font_height) // 2  # use font_height instead of bbox height

    # Draw centered text according to whether it is multiline or not
    if "\n" in text:
        draw.multiline_text(xy=(x, y), text=text, fill=text_color, font=font, align="center")
    else:
        draw.text(xy=(x, y), text=text, fill=text_color, font=font, align="center") 

    # Uncomment below lines to save the image to check size properly
    # output_path = os.path.join(LIB_IMG_PATH, "pixelify_sans_text.png") 
    # image.save(output_path)
    # image.show()
    
    # Convert PIL Image 
    title_image = ctk.CTkImage(light_image=image,size=img_size) 
    
    # Convert to CTkImage
    return title_image