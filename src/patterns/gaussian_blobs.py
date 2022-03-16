import numpy as np


def gaus2d(x=0, y=0, mx=0, my=0, sx=1, sy=1):
    return 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))


def norm(data):
    min_mat = np.min(data)
    max_mat = np.max(data)
    return (data - min_mat) / (max_mat - min_mat)


class GaussianBlobs:
    def __init__(self, number_of_blobs, size_range, color):
        self.number_of_blobs = number_of_blobs
        self.size_range = size_range
        self.color = color

    def draw(self, frame):
        img = frame.image
        # lab = frame.label
        height, width = img.shape[:2]
        g_masks = None
        for i in range(self.number_of_blobs):
            x = np.linspace(0, width, width)
            y = np.linspace(0, height, height)
            mx = np.random.randint(width)
            my = np.random.randint(height)
            sx = np.random.randint(self.size_range[0], self.size_range[1])
            sy = np.random.randint(self.size_range[0], self.size_range[1])
            x, y = np.meshgrid(x, y) # get 2D variables instead of 1D
            g_m = gaus2d(x, y, mx, my, sx, sy)
            if g_masks is None:
                g_masks = g_m
            else:
                g_masks += g_m

        g_masks = norm(g_masks)

        img[:, :, 0] = g_masks * self.color[0]
        img[:, :, 1] = g_masks * self.color[1]
        img[:, :, 2] = g_masks * self.color[2]

        frame.image = img
        return frame


