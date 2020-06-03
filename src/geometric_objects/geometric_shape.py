import numpy as np


class GeometricShape(object):
    def __init__(self, cfg):
        self.cfg = cfg

        self.position = [None, None]
        self.size = None
        self.orientation = None

    def new(self):
        self.position = self.new_position()
        self.size = self.new_size()
        self.orientation = self.new_orientation()

    def _create_new_parameter(self, opt, current_parameter):
        if type(opt) is list:
            return np.random.randint(int(opt[0]*100), int(opt[1]*100)) / 100
        else:
            if opt == "random" or (opt == "static" and current_parameter is None):
                return np.random.randint(100) / 100
            elif opt == "static":
                return current_parameter
            else:
                raise ValueError("Option: {} not known!".format(opt))

    def new_position(self):
        opt = self.cfg["position"]
        return [self._create_new_parameter(opt, self.position[0]), self._create_new_parameter(opt, self.position[1])]

    def new_size(self):
        opt = self.cfg["size"]
        return self._create_new_parameter(opt, self.size)

    def new_orientation(self):
        opt = self.cfg["orientation"]
        if opt == "random":
            opt = [0, 3.60]
        orient = self._create_new_parameter(opt, self.orientation)
        orient = orient / 1.80 * np.pi
        return orient

    def draw(self, frame):
        print("Not Implemented yet..")

