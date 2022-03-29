from PIL import ImageDraw, Image
import numpy as np
from src.geometric_objects.geometric_shape import GeometricShape


class Circle(GeometricShape):
    desc = "Circle"
    
    def __init__(self,
                 label,
                 init_color,
                 size_option,
                 position_option,
                 color_deviation=0.0,
                 texture=None,
                 seed=2022
                 ):

        super(Circle, self).__init__(
            label=label,
            init_color=init_color,
            size_option=size_option,
            position_option=position_option,
            color_deviation=color_deviation,
            texture=texture,
            seed=seed
        )

    def draw(self, frame):
        self.new()

        img = frame.image.astype(np.uint8)
        canvas = Image.fromarray(np.zeros(img.shape, dtype=np.uint8))
        lab = Image.fromarray(frame.label.astype(np.uint8))

        x_c, y_c = self.position
        r = self.size
        box_rel = [x_c - 0.5 * r, y_c - 0.5 * r, x_c + 0.5 * r, y_c + 0.5 * r]

        box = [
            (int(box_rel[0] * frame.w), int(box_rel[1] * frame.h)),
            (int(box_rel[2] * frame.w), int(box_rel[3] * frame.h))
        ]
        draw_i = ImageDraw.Draw(canvas)
        draw_i.ellipse(box, fill=self.color)
        del draw_i

        rr, cc = np.where(np.max(np.array(canvas), axis=2) > 0)
        frame = self.add_object(frame, rr, cc)

        if self.label_id is not None:
            draw_l = ImageDraw.Draw(lab)
            draw_l.ellipse(box, fill=self.label_id)
            del draw_l

        frame.label = np.array(lab)
        return frame
