import matplotlib.pyplot as plt
import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape


class Rectangle(GeometricShape):
    def __init__(self,
                 label,
                 init_color,
                 size_option,
                 position_option,
                 aspect_ratio_option,
                 color_deviation=0.0,
                 texture=None
                 ):

        super(Rectangle, self).__init__(
            label=label,
            init_color=init_color,
            size_option=size_option,
            position_option=position_option,
            color_deviation=color_deviation,
            texture=texture
        )
        self.aspect_ratio_option = aspect_ratio_option
        self.aspect_ratio = None
        self.aspect_ratio = self.new_aspect_ratio()

    def new_aspect_ratio(self):
        opt = self.aspect_ratio_option
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

        canvas = np.zeros((img.shape[0], img.shape[1]))
        canvas[int(box[1] * frame.h):int(box[3] * frame.h),
               int(box[0] * frame.w):int(box[2] * frame.w)] = 1

        rr, cc = np.where(canvas > 0)

        frame = self.add_object(frame, rr, cc)
        if self.label_id is not None:
            lab[int(box[1] * frame.h):int(box[3] * frame.h),
                int(box[0] * frame.w):int(box[2] * frame.w),
                :] = self.label_id
            frame.label = np.array(lab)
        return frame
