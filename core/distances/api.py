import numpy as np
from .registry import get_distance_metric

def getInstance(metric_name: str) -> object:
    """Retrieve an instance of a distance metric by name."""
    metric_class = get_distance_metric(metric_name)
    match metric_name.lower():
        case "minkowski":
            return metric_class(p=3)  # Default p=3 for Minkowski
        case _:
            return metric_class()

def compute(a: np.ndarray, b: np.ndarray, metric_name: str) -> float:
    """Compute the distance between two vectors a and b using the specified metric."""
    metric_instance =getInstance(metric_name)
    return metric_instance.compute(a, b)
def distance(x:int, y:int,s:int,t:int, metric_name: str) -> int:
    """Compute the distance between two points (x,y) and (s,t) using the specified metric."""
    metric_instance =getInstance(metric_name)
    return metric_instance.distance(x, y, s, t)
