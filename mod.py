# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:45:56 2020

@author: Danny
"""
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import config

config.SRC_TRAIN_DIR = askdirectory(title='Select Folder Containing WSI')
basefolder = os.path.dirname(config.SRC_TRAIN_DIR)
newfolder = config.SRC_TRAIN_DIR.split("/")[-1] + " Tiles"
config.BASE_DIR = os.path.join(basefolder,newfolder)
print(config.BASE_DIR)
config.TRAIN_PREFIX = "TR-"
config.SRC_TRAIN_EXT = "ndpi"
config.DEST_TRAIN_SUFFIX = ""  # Example: "train-"
config.DEST_TRAIN_EXT = "jpg"
config.SCALE_FACTOR = 32
config.DEST_TRAIN_DIR = os.path.join(config.BASE_DIR, "training_" + config.DEST_TRAIN_EXT)

