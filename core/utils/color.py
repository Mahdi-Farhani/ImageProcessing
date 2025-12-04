import numpy as np

class ColorImageUtility:
    @staticmethod
    def rgb_to_grayscale(image: np.ndarray) -> np.ndarray:
        """Convert an RGB image to grayscale."""
        if len(image.shape) != 3 or image.shape[2] != 3:
            raise ValueError("Input image must be an RGB image with 3 channels.")
        return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    