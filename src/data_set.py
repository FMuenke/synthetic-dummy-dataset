import os
from tqdm import tqdm
from copy import deepcopy
from src.frame import Frame

from src.background import Background
from src.noise import NoiseGroup


class DataSet:
    def __init__(self, options):
        self.options = options

        self.num_images = options["n_images"]

        self.objects = options["objects"]

        if "background_config" not in options:
            options["background_config"] = {}
        self.background_config = options["background_config"]

        if "noise_config" not in options:
            options["noise_config"] = {}
        self.noise_config = options["noise_config"]

    def __str__(self):
        s = deepcopy(self.options)
        if "objects" in s:
            s["objects"] = [str(o) for o in self.objects]
        if "noise_config" in s:
            if "operations" in s["noise_config"]:
                s["noise_config"]["operations"] = [str(n) for n in self.noise_config["operations"]]
        return str(s)

    def create(self, data_directory):
        """
        Function to create specified DataSet
        Args:
            data_directory: Path to the directory where the data set is created

        Returns:

        """
        i_dir = os.path.join(data_directory, "images")
        l_dir = os.path.join(data_directory, "labels")

        if not os.path.isdir(data_directory):
            os.mkdir(data_directory)

        if not os.path.isdir(i_dir):
            os.mkdir(i_dir)

        if not os.path.isdir(l_dir):
            os.mkdir(l_dir)

        background = Background(self.background_config)
        noise = NoiseGroup(self.noise_config)
        print(str(self))
        print("Creating the DataSet...")
        for i in tqdm(range(self.num_images)):
            frame_id = "frame_{}".format(i)
            frame = Frame(self.options)
            frame = background.draw(frame)
            for o in self.objects:
                frame = o.draw(frame)
            frame = noise.draw(frame)
            frame.write(os.path.join(i_dir, frame_id + ".png"),
                        os.path.join(l_dir, frame_id + ".png"))
        print("DataSet was successfully created at {}".format(data_directory))
        with open(os.path.join(data_directory, "description.txt"), "w") as f:
            f.write(str(self))
