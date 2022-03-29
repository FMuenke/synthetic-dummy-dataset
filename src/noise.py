import cv2
import numpy as np


class ChannelShift:
    def __init__(self, intensity, seed=2022):
        self.name = "channel_shift"
        self.intensity = intensity
        self.seed = seed
        self.rng = np.random.default_rng(seed)

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {"intensity": self.intensity, "seed": self.seed}

    def apply(self, img):
        height, width, ch = img.shape
        img = img.astype(np.float32)
        for i in range(ch):
            img[:, :, i] += self.rng.integers(255) * self.intensity * self.rng.choice([1, -1])
        img = np.clip(img, 0, 255)
        return img.astype(np.uint8)
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)


class Stripes:
    def __init__(self, horizontal, vertical, space, width, intensity):
        self.name = "stripes"
        self.horizontal = horizontal
        self.vertical = vertical
        self.space = space
        self.width = width
        self.intensity = intensity

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {
            "horizontal": self.horizontal,
            "vertical": self.vertical,
            "space": self.space, "width": self.width,
            "intensity": self.intensity,
        }

    def apply(self, img):
        h, w, c = img.shape
        g_h = int(h / self.width)
        g_w = int(w / self.width)
        mask = np.zeros([g_h, g_w, c])

        if self.horizontal:
            mask[::self.space, :, :] = self.intensity
        if self.vertical:
            mask[:, ::self.space, :] = self.intensity

        mask = cv2.resize(mask, (w, h), interpolation=cv2.INTER_NEAREST)
        img = mask.astype(np.float32) + img.astype(np.float32)
        return np.clip(img, 0, 255).astype(np.uint8)
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)


class Blurring:
    def __init__(self, kernel=9, randomness=5, seed=2022):
        self.name = "blurring"
        self.kernel = kernel
        self.randomness = randomness
        self.seed = seed
        self.rng = np.random.default_rng(seed)

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {"kernel": self.kernel, "randomness": self.randomness,
                "seed": self.seed}

    def apply(self, img):
        k = self.kernel + self.rng.integers(-self.randomness, self.randomness)
        img = cv2.blur(img.astype(np.float32), ksize=(k, k))
        return img.astype(np.uint8)
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)


class NeedsMoreJPG:
    def __init__(self, percentage, randomness, seed=2022):
        self.percentage = percentage
        self.randomness = randomness
        self.seed = seed
        self.rng = np.random.default_rng(seed)

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {"percentage": self.percentage, "randomness": self.randomness,
                "seed": self.seed}

    def apply(self, img):
        h, w = img.shape[:2]
        p = self.percentage + self.rng.integers(-self.randomness, self.randomness)
        img = cv2.resize(img, (int(w * p / 100), int(h * p / 100)), interpolation=cv2.INTER_NEAREST)
        img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
        return img
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)


class SaltNPepper:
    def __init__(self, max_delta, grain_size, seed=2022):
        self.max_delta = max_delta
        self.grain_size = grain_size
        self.seed = seed
        self.rng = np.random.default_rng(seed)

    def __str__(self):
        return str(self.to_json())

    def to_json(self):
        return {"max_delta": self.max_delta, "grain_size": self.grain_size,
                "seed": self.seed}

    def apply(self, img):
        h, w, c = img.shape
        snp_h = int(h / self.grain_size)
        snp_w = int(w / self.grain_size)
        snp = self.rng.integers(-self.max_delta, self.max_delta, size=[snp_h, snp_w, c])
        snp = cv2.resize(snp, (w, h), interpolation=cv2.INTER_NEAREST)
        img = img.astype(np.int) + snp
        return np.clip(img, 0, 255).astype(np.uint8)
    
    @classmethod
    def from_config(cls, config):
        return cls(**config)


class NoiseGroup:
    def __init__(self, config):
        self.mode = config["mode"]
        self.operations = config["operations"]

    def draw(self, frame):
        img = np.array(frame.image, np.uint8)
        for op in self.operations:
            img = op.apply(img)
        frame.image = img
        return frame
