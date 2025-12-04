import numpy as np
from .base import DistanceMetric

class EuclideanDistance(DistanceMetric):
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Euclidean distance between two vectors a and b."""
        return np.linalg.norm(a - b)
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Euclidean distance between two points (x,y) and (s,t)."""
        return int(((x - s) ** 2 + (y - t) ** 2) ** 0.5)