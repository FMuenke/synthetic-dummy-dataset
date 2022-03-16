import argparse
from src.data_set import DataSet
from src import noise
from src.geometric_objects import Ellipse, Circle, Rectangle


def main(args_):
    r = Rectangle(
        label=(255, 255, 255),
        init_color=(0, 0, 200),
        position_option=[0.2, 0.8],
        aspect_ratio_option=[0.1, 0.8],
        size_option=[0.25, 0.60],
        color_deviation=0.2,
    )
    e = Ellipse(
        label=(255, 255, 255),
        init_color=(0, 150, 0),
        position_option=[0.2, 0.8],
        size_option=[0.1, 0.40],
        orientation_option="random",
        eccentricity_option=[0.1, 0.9],
        color_deviation=0.3,
        texture=noise.SaltNPepper(50, 4)
    )
    c = Circle(
        label=(255, 255, 255),
        init_color=(200, 0, 0),
        position_option=[0.2, 0.8],
        size_option=[0.25, 0.60],
        color_deviation=0.2,
    )

    cfg = {
        "n_images": 100,
        "image_width": 400,
        "image_height": 400,
        "objects": [
            Ellipse(
                label=(255, 255, 255),
                init_color=(0, 150, 0),
                position_option=[0.2, 0.8],
                size_option=[0.1, 0.40],
                orientation_option="random",
                eccentricity_option=[0.1, 0.9],
                color_deviation=0.3,
                texture=noise.SaltNPepper(50, 4)
        )],
        "background_config": {
            "mode": "random_gaussian",
            "color": [(150, 25, 150), (150, 25, 25), (25, 150, 150)],
            "number_of_objects": [50, 200],
            "size": [0.01, 0.2]
        },
        "noise_config": {
            "mode": "random",
            "operations": [
                noise.Blurring(7, randomness=3),
                noise.SaltNPepper(10, 8),
                noise.ChannelShift(0.10)
                # noise.NeedsMoreJPG(50, 10),
            ]
        }
    }

    df = args_.data_set_folder
    data_set = DataSet(cfg)
    data_set.create(df)


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
