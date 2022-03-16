from PIL import ImageDraw, Image
import numpy as np
import cv2
from src.geometric_objects.geometric_shape import GeometricShape


class Line(GeometricShape):
    def __init__(self,
                 label,
                 init_color,
                 size_option,
                 # position_option,
                 # orientation_option,
                 color_deviation=0.0,
                 ):

        super(Line, self).__init__(
            label=label,
            init_color=init_color,
            size_option=size_option,
            # position_option=position_option,
            # orientation_option=orientation_option,
            color_deviation=color_deviation,
        )

    def draw(self, frame):
        self.new()

        img = frame.image.astype(np.uint8)
        lab = Image.fromarray(frame.label.astype(np.uint8))
        height, width = img.shape[:2]
        orientation = np.random.choice(["horizontal", "vertical"])

        if orientation == "horizontal":
            start_point = (np.random.randint(width), 0)
            end_point = (np.random.randint(width), height)
        else:
            start_point = (0, np.random.randint(height))
            end_point = (width, np.random.randint(height))

        img = cv2.line(img, start_point, end_point, color=self.color, thickness=int(self.size))

        if self.label_id is not None:
            lab = cv2.line(lab, start_point, end_point, color=self.label_id, thickness=int(self.size))

        frame.image = np.array(img)
        frame.label = np.array(lab)
        return frame
