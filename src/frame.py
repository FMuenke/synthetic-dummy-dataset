import numpy as np
from PIL import Image
from copy import copy


class Frame:
    def __init__(self, cfg):
        self.h = copy(cfg["image_height"])
        self.w = copy(cfg["image_width"])
        self.image = np.zeros((self.h, self.w, 3), dtype=np.uint8)
        self.label = np.zeros((self.h, self.w, 3), dtype=np.uint8)

    def write(self, frame_image_path, frame_label_path):
        img = Image.fromarray(self.image)
        img.save(frame_image_path)
        lab = Image.fromarray(self.label)
        lab.save(frame_label_path)
