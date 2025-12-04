import numpy as np
from core.transform.base import TransformBase


class FourierTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply Fourier transformation to the input data."""
        f_transform = np.fft.fft2(data)
        f_shifted = np.fft.fftshift(f_transform)
        magnitude_spectrum = 20 * np.log(np.abs(f_shifted) + 1)  # Added +1 to avoid log(0)
        return np.array(magnitude_spectrum, dtype=np.uint8)