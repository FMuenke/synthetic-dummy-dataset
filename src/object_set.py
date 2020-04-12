from src.ellipse import Ellipse
from src.rectangle import Rectangle


class ObjectSet:
    def __init__(self, object_config):
        self.members = []

        for o in object_config:
            if "ellipse" in o:
                self.members.append(Ellipse(object_config[o]))
            elif "rectangle" in o:
                self.members.append(Rectangle(object_config[o]))

    def draw(self, frame):
        for o in self.members:
            o.draw(frame)
        return frame
