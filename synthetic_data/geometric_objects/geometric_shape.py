import numpy as np


class GeometricShape(object):
    desc = "GeometricShape"

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
        self.label_id = label

        self.init_color = init_color
        self.size_option = size_option
        self.position_option = position_option
        self.orientation_option = orientation_option
        self.eccentricity_option = eccentricity_option
        self.color_deviation = color_deviation

        self.color = None
        self.position = [None, None]
        self.size = None
        self.orientation = None
        self.eccentricity = None
        self.texture = texture
        self.rng = np.random.default_rng(seed)

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {
            "name": self.desc,
            "color": self.init_color,
            "color_deviation": self.color_deviation,
        }

    def new(self):
        self.position = self.new_position()
        self.size = self.new_size()
        self.color = self.new_color()
        self.eccentricity = self.new_eccentricity()
        self.orientation = self.new_orientation()

    def new_eccentricity(self):
        opt = self.eccentricity_option
        eccentricity = self._create_new_parameter(opt, self.eccentricity)
        return eccentricity

    def new_orientation(self):
        opt = self.orientation_option
        if opt == "random":
            opt = [0, 3.60]
        orient = self._create_new_parameter(opt, self.orientation)
        orient = orient / 1.80 * np.pi
        return orient

    def new_color(self):
        r, g, b = self.init_color
        if self.color_deviation > 0:
            dr = self.rng.integers(self.color_deviation) * self.rng.choice([1, -1])
            dg = self.rng.integers(self.color_deviation) * self.rng.choice([1, -1])
            db = self.rng.integers(self.color_deviation) * self.rng.choice([1, -1])
            r = np.clip(r + dr, 0, 255)
            g = np.clip(g + dg, 0, 255)
            b = np.clip(b + db, 0, 255)
        return int(r), int(g), int(b)

    def _create_new_parameter(self, opt, current_parameter):
        if type(opt) is list:
            return self.rng.integers(int(opt[0]*100), int(opt[1]*100)) / 100
        else:
            if opt == "random" or (opt == "static" and current_parameter is None):
                return self.rng.integers(100) / 100
            elif opt == "static":
                return current_parameter
            else:
                raise ValueError("Option: {} not known!".format(opt))

    def new_position(self):
        opt = self.position_option
        return [self._create_new_parameter(opt, self.position[0]), self._create_new_parameter(opt, self.position[1])]

    def new_size(self):
        opt = self.size_option
        return self._create_new_parameter(opt, self.size)

    def add_object(self, frame, rr, cc):
        object_only = np.zeros(frame.image.shape)
        object_only[rr, cc, :] = self.color
        if self.texture is not None:
            object_only = self.texture.apply(object_only)
        frame.image[rr, cc, :] = object_only[rr, cc, :]
        return frame

    def draw(self, frame):
        print("Not Implemented yet..")
        
    @classmethod
    def from_config(cls, config):
        _ = config.pop("name", None) # remove name from config in case key is present
        return cls(**config)

