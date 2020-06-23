from PIL import Image, ImageDraw
import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape


class Rectangle(GeometricShape):
    def __init__(self, cfg):
        self.color = cfg["color"]
        self.label_id = cfg["label"]

        super(Rectangle, self).__init__(cfg)
        self.aspect_ratio = None
        self.aspect_ratio = self.new_aspect_ratio()

    def new_aspect_ratio(self):
        opt = self.cfg["aspect_ratio"]
        aspect_ratio = self._create_new_parameter(opt, self.aspect_ratio)
        return aspect_ratio

    def get_parameters(self):
        x_c, y_c = self.position
        height = self.size
        width = height * self.aspect_ratio
        x1 = x_c - 0.5 * width
        y1 = y_c - 0.5 * height
        x2 = x_c + 0.5 * width
        y2 = y_c + 0.5 * height
        return [x1, y1, x2, y2]

    def draw(self, frame):
        self.new()
        self.aspect_ratio = self.new_aspect_ratio()

        box = self.get_parameters()
        img = np.copy(frame.image.astype(np.uint8))
        lab = np.copy(frame.label.astype(np.uint8))

        img[int(box[1] * frame.h):int(box[3] * frame.h),
            int(box[0] * frame.w):int(box[2] * frame.w),
            :] = self.color

        frame.image = np.array(img)
        if self.label_id is not None:
            lab[int(box[1] * frame.h):int(box[3] * frame.h),
                int(box[0] * frame.w):int(box[2] * frame.w),
                :] = self.label_id
        return frame
