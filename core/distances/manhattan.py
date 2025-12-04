import numpy as np
from .base import DistanceMetric

class ManhattanDistance(DistanceMetric):
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Manhattan distance between two vectors a and b."""
        return np.sum(np.abs(a - b))
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Manhattan distance between two points (x,y) and (s,t)."""
        return abs(x - s) + abs(y - t)