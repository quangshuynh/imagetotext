"""
Image to Text
03/15/2024
author: Quang Huynh
"""

from PIL import Image

def convertToAscii(image, type, saveas, scale):
    scale = int(scale)  # convert scale to integer