from synthetic_data.geometric_objects.ellipse import Ellipse
from synthetic_data.geometric_objects.rectangle import Rectangle
from src.geometric_objects.circle import Circle


class ObjectSet:
    def __init__(self, object_config):
        self.members = []

        for o in object_config:
            if "ellipse" in o:
                self.members.append(Ellipse(object_config[o]))
            elif "rectangle" in o:
                self.members.append(Rectangle(object_config[o]))
            elif "circle" in o:
                self.members.append(Circle(object_config[o]))
            else:
                raise ValueError("Object: {} could not be handled.".format(o))

    def draw(self, frame):
        for o in self.members:
            o.draw(frame)
        return frame
