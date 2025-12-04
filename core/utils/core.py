import numpy as np
from PIL import Image as image

class ImageUtility:
    @staticmethod
    def load_image(path: str) -> np.ndarray:
        """Load an image from the specified path and return it as a NumPy array."""
        img = image.open(path)
        return np.array(img)

    @staticmethod
    def save_image(image_array: np.ndarray, path: str) -> None:
        """Save a NumPy array as an image to the specified path."""
        img = image.fromarray(image_array)
        img.save(path)