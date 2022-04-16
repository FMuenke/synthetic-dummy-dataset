import json
import os
import argparse
from synthetic_data.data_set import DataSet


def main(args_):

    factor = 0.2

    cfg = {
        "n_images": 1,
        "image_width": 400,
        "image_height": 400,
        "objects": [{
            "name": "Ellipse",
            "label": (255, 255, 255),
            "init_color": (0, 150, 0),
            "position_option": [0.2, 0.8],
            "size_option": [0.1, 0.40],
            "orientation_option": "random",
            "eccentricity_option": [0.1, 0.9],
            "color_deviation": 16,
            "texture": {
                "name": "SaltNPepper",
                "max_delta": 40,
                "grain_size": 4
                }
            }],
        "background_config": {
            "mode": "random_gaussian",
            "color": [(150, 25, 150), (150, 25, 25), (25, 150, 150)],
            "number_of_objects": [50, 200],
            "size": [10, 30]
        },
        "noise_config": {
            "mode": "random",
            "operations": [
                {"name": "Blurring", "kernel": int(400 * factor)},
                {"name": "SaltNPepper", "max_delta": int(254 * factor), "grain_size": 8},
                {"name": "ChannelShift", "intensity": int(254 * factor)},
            ]
        },
    }
    
    if args_.config_file:
        with open(args_.config_file, "r") as file:
            cfg = json.load(file)

    df = args_.data_set_folder
    data_set = DataSet(cfg)
    if not os.path.isdir(df):
        os.mkdir(df)
    data_set.create(os.path.join(df, "train"))
    data_set.create(os.path.join(df, "test"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_set_folder",
        "-df",
        default="./data/train",
        help="Path to directory with dataset",
    )
    parser.add_argument(
        "--config_file", 
        "-c",
        default=None,
        help="Path to config json file to use for dataset creation"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)
