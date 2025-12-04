import numpy as np
from .base import DistanceMetric

class HammingDistance(DistanceMetric):
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Hamming distance between two vectors a and b."""
        return np.sum(a != b)
    
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Hamming distance between two points (x,y) and (s,t)."""
        dist = 0
        if x != s:
            dist += 1
        if y != t:
            dist += 1
        return dist