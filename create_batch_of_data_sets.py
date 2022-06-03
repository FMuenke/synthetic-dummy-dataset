import os
import argparse
from synthetic_data.data_set import DataSet


def create_ds(df, factor):
    cfg = {
        "n_images": 512,
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
                "min_delta": 40,
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
                {"name": "SaltNPepper", "max_delta": int(255 * factor), "grain_size": 8},
                {"name": "ChannelShift", "intensity": int(255 * factor)},
            ]
        },
    }

    data_set = DataSet(cfg)
    if not os.path.isdir(df):
        os.mkdir(df)
    data_set.create(os.path.join(df, "train"))
    data_set.create(os.path.join(df, "test"))


def main(args_):
    base_dir = args_.data_set_folder
    for f in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 100]:
        data_set_folder = os.path.join(base_dir, "synth_A{:03d}".format(f))
        print(data_set_folder)
        create_ds(data_set_folder, f/100)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_set_folder",
        "-df",
        default="./data/train",
        help="Path to directory with dataset",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)
