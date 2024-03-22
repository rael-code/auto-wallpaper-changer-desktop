import ctypes
import os
import random
import time

# directory containing wallpaper images
wallpaper_dir = r"C:\Users\User\Desktop\Coding\Wallpaper_D"


# function to set the wallpaper
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)


# to get a list of image files in the wallpaper directory
wallpapers = [os.path.join(wallpaper_dir, filename) for filename in os.listdir(wallpaper_dir) if
              filename.endswith((".jpg", ".jpeg", ".png", ".bmp"))]

# main loop to change wallpaper 
while True:
    # program to choose random wallpaper from the list
    random_wallpaper = random.choice(wallpapers)

    # set the chosen wallpaper as desktop background
    set_wallpaper(random_wallpaper)

    # print debug information
    print(f"Changed wallpaper to: {random_wallpaper}")

    # sleep timer (e.g. 10 minutes)
    time.sleep(600)  # Sleep for 600 seconds (10 minutes)
