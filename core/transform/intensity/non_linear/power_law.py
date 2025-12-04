import numpy as np
from core.transform.base import TransformBase

class PowerLawTransform(TransformBase):
    def apply(self, data: np.ndarray, gamma: float = 2.2) -> np.ndarray:
        """Apply power-law (gamma) transformation to the input data."""
        data = data.astype(np.float32)

        # Normalize input to 0–1
        data_norm = data / 255.0

        # Apply power-law transform
        power_law_result = np.power(data_norm, gamma)

        # Denormalize
        out = power_law_result * 255.0

        return out.astype(np.uint8)