import numpy as np
from core.transform.base import TransformBase

class NegativeTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply negative transformation to the input data."""
        return 255 - data
