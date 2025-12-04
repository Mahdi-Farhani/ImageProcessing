import numpy as np
from .base import DistanceMetric

class MinkowskiDistance(DistanceMetric):
    def __init__(self, p: int):
        """Initialize the Minkowski distance with order p."""
        self.p = p

    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Minkowski distance between two vectors a and b."""
        return np.sum(np.abs(a - b) ** self.p) ** (1 / self.p)
    
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Minkowski distance between two points (x,y) and (s,t)."""
        return int((abs(x - s) ** self.p + abs(y - t) ** self.p) ** (1 / self.p))