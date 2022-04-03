import cv2
import numpy as np
from PIL import Image


class Frame:
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.image = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        self.label = np.zeros((self.h, self.w, 3), dtype=np.uint8)

    def write(self, frame_image_path, frame_label_path):
        img = Image.fromarray(self.image)
        img.save(frame_image_path)
        lab = Image.fromarray(self.label)
        lab.save(frame_label_path)

    def copy(self):
        new_frame = Frame(self.h, self.w)
        new_frame.image = np.copy(self.image)
        new_frame.label = np.copy(self.label)
        return new_frame
