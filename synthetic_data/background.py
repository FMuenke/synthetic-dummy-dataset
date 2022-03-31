import numpy as np
from src.geometric_objects import Circle, Rectangle, Ellipse, Line
from src.patterns.gaussian_blobs import GaussianBlobs


def pick_color(color):
    if color is None:
        color = (np.random.randint(255), np.random.randint(255), np.random.randint(255))
    elif type(color) is list:
        color_id = np.random.randint(len(color))
        color = color[color_id]
    return color

def generate_random_object(color, size):
    color = pick_color(color)

    if size is None:
        min_size = (np.random.randint(99) + 1) / 100
        max_size = (np.random.randint(99) + 1) / 100
        size = [
            min_size,
            np.clip(max_size, min_size + 1, 1),
        ]

    possible_objects = [
            Ellipse(
                label=None,
                init_color=color,
                position_option="random",
                size_option=size,
                orientation_option="random",
                eccentricity_option="random",
                color_deviation=0.6,
            ),
            Circle(
                label=None,
                init_color=color,
                position_option="random",
                size_option=size,
                color_deviation=0.6,
            ),
            Rectangle(
                label=None,
                init_color=color,
                position_option="random",
                aspect_ratio_option="random",
                size_option=size,
                color_deviation=0.6,
            )
        ]
    return np.random.choice(possible_objects)


class Background:
    def __init__(self, cfg):
        self.cfg = cfg
        if "color" not in cfg:
            cfg["color"] = None
        self.color = cfg["color"]
        if "size" not in cfg:
            cfg["size"] = None
        self.size = cfg["size"]
        if "mode" not in cfg:
            cfg["mode"] = ""
        self.mode = cfg["mode"]
        if "number_of_objects" not in cfg:
            cfg["number_of_objects"] = [10, 20]
        self.number_of_objects = cfg["number_of_objects"]

    def draw(self, frame):
        if self.mode == "random_objects":
            for i in range(np.random.randint(self.number_of_objects[0], self.number_of_objects[1])):
                obj = generate_random_object(self.color, self.size)
                frame = obj.draw(frame)
            return frame
        elif self.mode == "random_lines":
            for i in range(np.random.randint(self.number_of_objects[0], self.number_of_objects[1])):
                line = Line(label=None, init_color=pick_color(self.color), size_option=[1, 10], color_deviation=0.2)
                frame = line.draw(frame)
            return frame
        elif self.mode == "random_gaussian":
            g_blobs = GaussianBlobs(
                np.random.randint(self.number_of_objects[0], self.number_of_objects[1]),
                size_range=[10, 30],
                color=pick_color(self.color)
            )
            frame = g_blobs.draw(frame)
            return frame
        else:
            return frame
