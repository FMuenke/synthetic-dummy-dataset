from PIL import ImageDraw, Image
import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape
from skimage.draw import ellipse


class Ellipse(GeometricShape):
    def __init__(self, cfg):
        super(Ellipse, self).__init__(cfg)
        self.color = cfg["color"]
        self.label_id = cfg["label"]
        self.shape_factor = 0.2
        self.param = [None, None, None, None, None]

    def new_shape(self):
        opt = self.cfg["shape_opt"]
        x_c, y_c = self.position
        semi_x, semi_y = self.size, self.size
        rot = 0
        if opt == "random":
            semi_x += np.random.randint(int(self.shape_factor * 100)) / 100 - 0.5 * self.shape_factor
            semi_y += np.random.randint(int(self.shape_factor * 100)) / 100 - 0.5 * self.shape_factor
            rot += np.random.randint(100) / 100 * 2 * np.pi - np.pi
        elif opt == "static":
            pass
        else:
            raise ValueError("Shape Option: {} not known.".format(opt))

        self.param = [x_c, y_c, semi_x, semi_y, rot]

    def draw(self, frame):
        self.new_position()
        self.new_shape()

        rr, cc = ellipse(r=self.param[0] * frame.w,
                         c=self.param[1] * frame.h,
                         r_radius=self.param[2] * frame.w,
                         c_radius=self.param[3] * frame.h,
                         rotation=self.param[4],
                         shape=[frame.h, frame.w])

        frame.image[rr, cc, :] = self.color
        frame.label[rr, cc, :] = self.label_id
        return frame
