from abc import ABC,abstractmethod
import numpy as np

class DistanceMetric(ABC):
    @abstractmethod
    def compute(self, a: np.ndarray, b: np.ndarray) -> float:
        """Compute the distance between two vectors a and b."""
        pass
    
    @abstractmethod
    def distance(self, x:int, y:int,s:int,t:int) -> int:
        """Compute some other metric between two points (x,y) and (s,t)."""
        pass

