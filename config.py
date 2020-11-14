# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:43:55 2020

@author: Danny
"""
import os

BASE_DIR = os.path.join(".", "dat")
TRAIN_PREFIX = "TR-"
SRC_TRAIN_DIR = os.path.join(BASE_DIR, 'training_slides')
SRC_TRAIN_EXT = "ndpi"
DEST_TRAIN_SUFFIX = ""  # Example: "train-"
DEST_TRAIN_EXT = "jpg"
SCALE_FACTOR = 32
DEST_TRAIN_DIR = os.path.join(BASE_DIR, "training_" + DEST_TRAIN_EXT)