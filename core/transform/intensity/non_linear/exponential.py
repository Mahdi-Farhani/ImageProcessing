import numpy as np
from core.transform.base import TransformBase

class ExponentialTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply exponential transformation to the input data."""
        data = data.astype(np.float32)

        # Normalize input to 0–1
        data_norm = data / 255.0

        # Apply exponential transform safely
        exp_result = np.exp(data_norm) - 1  

        # Denormalize
        max_val = np.max(exp_result)
        if max_val == 0:
            return np.zeros_like(data_norm, dtype=np.uint8)

        out = (exp_result / max_val) * 255.0

        return out.astype(np.uint8)