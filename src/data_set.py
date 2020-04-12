import os
from tqdm import tqdm
from src.frame import Frame

from src.object_set import ObjectSet


class DataSet:
    def __init__(self, options):
        self.options = options

        self.num_images = options["n_images"]

        self.object_config = options["object_config"]

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

        o_set = ObjectSet(self.object_config)

        print("Creating the DataSet...")
        for i in tqdm(range(self.num_images)):
            frame_id = "frame_{}".format(i)
            frame = Frame(self.options)
            frame = o_set.draw(frame)
            frame.write(os.path.join(i_dir, frame_id + ".jpg"),
                        os.path.join(l_dir, frame_id + ".png"))
        print("DataSet was successfully created at {}".format(data_directory))
