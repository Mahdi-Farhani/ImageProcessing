import numpy as np
from .base import DistanceMetric

class ChessBoardDistance(DistanceMetric):
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Chessboard distance between two vectors a and b."""
        return np.max(np.abs(a - b))
    
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Chessboard distance between two points (x,y) and (s,t)."""
        return max(abs(x - s), abs(y - t))