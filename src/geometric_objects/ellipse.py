import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape
from skimage.draw import ellipse


class Ellipse(GeometricShape):
    def __init__(self, cfg):
        super(Ellipse, self).__init__(cfg)
        self.color = cfg["color"]
        self.label_id = cfg["label"]
        self.eccentricity = None
        self.eccentricity = self.new_eccentricity()

    def new_eccentricity(self):
        opt = self.cfg["eccentricity"]
        eccentricity = self._create_new_parameter(opt, self.eccentricity)
        return eccentricity

    def get_parameters(self):
        x_c, y_c = self.position
        major = self.size
        if self.eccentricity == 0:
            minor = major
        elif self.eccentricity == 1:
            minor = 0.0001
        else:
            minor = np.sqrt((1 - self.eccentricity**2) * major**2)
        semi_major = major / 2
        semi_minor = minor / 2
        return [x_c, y_c, semi_major, semi_minor, self.orientation]

    def draw(self, frame):
        self.new()
        self.eccentricity = self.new_eccentricity()

        param = self.get_parameters()
        rr, cc = ellipse(r=param[0] * frame.w,
                         c=param[1] * frame.h,
                         r_radius=param[2] * frame.w,
                         c_radius=param[3] * frame.h,
                         rotation=param[4],
                         shape=[frame.h, frame.w])

        frame.image[rr, cc, :] = self.color
        if self.label_id is not None:
            frame.label[rr, cc, :] = self.label_id
        return frame
