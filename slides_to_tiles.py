# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 17:54:01 2020

@author: Danny
"""
import os
from PIL import Image
import time
import config
import mod
import tiles
import slide
import util
import filter
Image.MAX_IMAGE_PIXELS = None
  
# Function to rename multiple files 
def rename(directory):
    
    for count, filename in enumerate(os.listdir(directory)): 
        extension = os.path.splitext(filename)[1]
        
        dst = str(count+10000) + extension
        src = directory +"\\" + filename 
        dst = directory +"\\" + dst 

        # rename() function will 
        # rename all the files
        os.rename(src, dst)        
    
    for count, filename in enumerate(os.listdir(directory)): 
        extension = os.path.splitext(filename)[1]
        
        dst = "TR-"+ str(count+1).zfill(4) + extension
        src = directory +"\\" + filename 
        dst = directory +"\\" + dst 

        # rename() function will 
        # rename all the files
        os.rename(src, dst) 

if __name__ == "__main__":
    
    rename(config.SRC_TRAIN_DIR)
    
    # slide.show_slide(1)
    # slide.slide_info(display_all_properties=True)
    # slide.slide_stats()

    # slide.training_slide_to_image(2)
    # img_path = slide.get_training_image_path(2)
    # img = slide.open_image(img_path)
    # img.show()

    # slide.slide_to_scaled_pil_image(4)[0].show()
    # slide.singleprocess_training_slides_to_images()
    # slide.multiprocess_training_slides_to_images()
    
    slide.singleprocess_training_slides_to_images()
    filter.singleprocess_apply_filters_to_images()
    tiles.singleprocess_filtered_images_to_tiles()
    
    # slide.multiprocess_training_slides_to_images()
    # filter.multiprocess_apply_filters_to_images()
    # tiles.multiprocess_filtered_images_to_tiles()