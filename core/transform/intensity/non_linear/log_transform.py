import numpy as np
from core.transform.base import TransformBase

class LogTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply logarithmic transformation to the input data."""
        c = 255 / np.log(1 + np.max(data))
        log_transformed = c * np.log(1 + data)
        return np.array(log_transformed, dtype=np.uint8)
    