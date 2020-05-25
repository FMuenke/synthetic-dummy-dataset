import numpy as np


class GeometricShape(object):
    def __init__(self, cfg):
        self.cfg = cfg
        self.position = [np.random.randint(100) / 100,
                         np.random.randint(100) / 100]

        s = self.cfg["size"]
        if type(s) == list:
            self.size = np.random.randint((abs(s[0] - s[1]) * 100)) / 100
        else:
            self.size = s

    def new_position(self):
        opt = self.cfg["position_opt"]
        if opt == "random":
            self.position = [np.random.randint(25, 75) / 100, np.random.randint(25, 75) / 100]
        elif opt == "static":
            pass
        else:
            raise ValueError("Position Option: {} not known!".format(opt))

    def new_size(self):
        opt = self.cfg["size_opt"]
        if opt == "random":
            self.size = np.random.randint(1, 100) / 100
        elif opt == "static":
            pass
        else:
            raise ValueError("Position Option: {} not known!".format(opt))

    def draw(self, frame):
        print("Not Implemented yet..")

