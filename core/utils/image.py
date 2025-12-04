import numpy as np
from PIL import Image as image
from core.utils import color as CU

class ImageCoreUtility:
    @staticmethod
    def load_image(path: str,grayscale: bool) -> np.ndarray:
        """Load an image from the specified path and return it as a NumPy array."""
        img = image.open(path)
        value = np.array(img)
        if (grayscale):
            value = CU.ColorImageUtility.rgb_to_grayscale(value)
        return value
    
    @staticmethod
    def load_image(path:str):
        img = image.open(path)
        rgb = np.array(img)
        gray = CU.ColorImageUtility.rgb_to_grayscale(rgb)
        return img,rgb, gray

    @staticmethod
    def save_image(image_array: np.ndarray, path: str) -> None:
        """Save a NumPy array as an image to the specified path."""
        img = image.fromarray(image_array)
        img.save(path)