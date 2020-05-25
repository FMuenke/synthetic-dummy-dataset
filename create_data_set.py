import argparse
from src.data_set import DataSet


def main(args_):

    cfg = {
        "n_images": 300,
        "image_width": 400,
        "image_height": 400,
        "object_config":
            {
                "ellipse": {
                    "label": (255, 0, 0),
                    "color": (0, 200, 0),
                    "size": 0.3,
                    "shape_opt": "random",
                    "position_opt": "random",
                    "size_opt": "random"
                },
                "rectangle_1": {
                    "label": None,
                    "color": (0, 0, 0),
                    "size": 0.3,
                    "shape_opt": "random",
                    "position_opt": "random",
                    "size_opt": "random"
                },
                "rectangle_2": {
                    "label": None,
                    "color": (0, 0, 0),
                    "size": 0.3,
                    "shape_opt": "random",
                    "position_opt": "random",
                    "size_opt": "random"
                },
                "rectangle_3": {
                    "label": None,
                    "color": (0, 0, 0),
                    "size": 0.3,
                    "shape_opt": "random",
                    "position_opt": "random",
                    "size_opt": "random"
                },
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
