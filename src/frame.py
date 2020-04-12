import numpy as np
from PIL import Image
from copy import copy


class Frame:
    def __init__(self, cfg):
        self.h = copy(cfg["image_height"])
        self.w = copy(cfg["image_width"])
        self.image = np.zeros((self.h, self.w, 3))
        self.label = np.zeros((self.h, self.w, 3))

    def write(self, frame_image_path, frame_label_path):
        i = Image.fromarray(self.image)
        i.save(frame_image_path)
        l = Image.fromarray(self.label)
        l.save(frame_label_path)

    def make_background(self):
        pass
