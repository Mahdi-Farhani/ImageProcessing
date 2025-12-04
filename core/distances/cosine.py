import numpy as np
from .base import DistanceMetric

class CosineDistance(DistanceMetric):
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the Cosine distance between two vectors a and b."""
        dot_product = np.dot(a, b)
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 1.0  # Define cosine distance as 1 if either vector is zero
        cosine_similarity = dot_product / (norm_a * norm_b)
        return 1 - cosine_similarity
    
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute the Cosine distance between two points (x,y) and (s,t)."""
        vec1 = np.array([x, y])
        vec2 = np.array([s, t])
        return int(self.compute(vec1, vec2) * 1000)  # Scale for integer representation
    