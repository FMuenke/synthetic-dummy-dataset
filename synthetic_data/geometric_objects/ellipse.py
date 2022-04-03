import numpy as np
from synthetic_data.geometric_objects.geometric_shape import GeometricShape
from skimage.draw import ellipse


class Ellipse(GeometricShape):
    desc = "Ellipse"

    def __init__(self,
                 label=None,
                 init_color=(0, 200, 0),
                 size_option="random",
                 position_option="random",
                 orientation_option="random",
                 eccentricity_option="random",
                 color_deviation=0.0,
                 texture=None,
                 seed=2022
                 ):
        super(Ellipse, self).__init__(
            label=label,
            init_color=init_color,
            size_option=size_option,
            position_option=position_option,
            orientation_option=orientation_option,
            eccentricity_option=eccentricity_option,
            color_deviation=color_deviation,
            texture=texture,
            seed=seed
        )

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
        self.orientation = self.new_orientation()

        param = self.get_parameters()
        rr, cc = ellipse(r=param[0] * frame.w,
                         c=param[1] * frame.h,
                         r_radius=param[2] * frame.w,
                         c_radius=param[3] * frame.h,
                         rotation=param[4],
                         shape=[frame.h, frame.w])
        self.add_object(frame, rr, cc)
        if self.label_id is not None:
            frame.label[rr, cc, :] = self.label_id
        return frame
