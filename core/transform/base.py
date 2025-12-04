from abc import ABC, abstractmethod
import numpy as np

class TransformBase(ABC):
    @abstractmethod
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply the transformation to the input data."""
        pass