import cv2
from synthetic_data import Frame
from synthetic_data.noise import SaltNPepper, ChannelShift, Blurring
from synthetic_data import geometric_objects
from synthetic_data.patterns.gaussian_blobs import GaussianBlobs


def main():
    f = Frame(height=400, width=400)

    back = GaussianBlobs(color=(150, 25, 150), number_of_blobs=120, size_range=[10, 30])
    cfg = {
        "name": "Ellipse",
        "label": (255, 255, 255),
        "init_color": (0, 150, 0),
        "position_option": [0.2, 0.8],
        "size_option": [0.1, 0.40],
        "orientation_option": "random",
        "eccentricity_option": [0.1, 0.9],
        "color_deviation": 50,
        "texture": SaltNPepper(50, 4),
        }
    e = getattr(geometric_objects, cfg["name"]).from_config(cfg)

    f = back.draw(f)
    cv2.imwrite("./background.jpg", f.image)
    f = e.draw(f)
    cv2.imwrite("./object.jpg", f.image)

    n_1 = SaltNPepper(max_delta=50, grain_size=8)
    n_2 = ChannelShift(intensity=100, seed=42)
    n_3 = Blurring(27, 1)

    f_1 = f.copy()
    f_1.image = n_1.apply(f_1.image)
    cv2.imwrite("./object_n1.jpg", f_1.image)

    f_1 = f.copy()
    f_1.image = n_2.apply(f_1.image)
    cv2.imwrite("./object_n2.jpg", f_1.image)

    f_1 = f.copy()
    f_1.image = n_3.apply(f_1.image)
    cv2.imwrite("./object_n3.jpg", f_1.image)


if __name__ == "__main__":
    main()
