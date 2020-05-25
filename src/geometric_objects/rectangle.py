from PIL import Image, ImageDraw
import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape


class Rectangle(GeometricShape):
    def __init__(self, cfg):
        self.color = cfg["color"]
        self.label_id = cfg["label"]

        super(Rectangle, self).__init__(cfg)
        self.shape_factor = 0.2
        self.box = [None, None, None, None]

    def new_shape(self):
        opt = self.cfg["shape_opt"]
        x_c, y_c = self.position
        w, h = self.size, self.size
        if opt == "random":
            w += np.random.randint(int(self.shape_factor * 100)) / 100 - 0.5 * self.shape_factor
            h += np.random.randint(int(self.shape_factor * 100)) / 100 - 0.5 * self.shape_factor
        elif opt == "static":
            pass
        else:
            raise ValueError("Shape Option: {} not known.".format(opt))

        x1 = x_c - 0.5 * w
        y1 = y_c - 0.5 * h
        x2 = x_c + 0.5 * w
        y2 = y_c + 0.5 * h
        self.box = [x1, y1, x2, y2]

    def draw(self, frame):
        self.new_position()
        self.new_shape()
        img = np.copy(frame.image.astype(np.uint8))
        lab = np.copy(frame.label.astype(np.uint8))

        img[int(self.box[1] * frame.h):int(self.box[3] * frame.h),
            int(self.box[0] * frame.w):int(self.box[2] * frame.w),
            :] = self.color

        frame.image = np.array(img)
        if self.label_id is not None:
            lab[int(self.box[1] * frame.h):int(self.box[3] * frame.h),
                int(self.box[0] * frame.w):int(self.box[2] * frame.w),
                :] = self.label_id
        return frame
