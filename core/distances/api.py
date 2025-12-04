import numpy as np
from .registry import get_distance_metric

def distance(a: np.ndarray, b: np.ndarray, metric_name: str) -> float:
    """Compute the distance between two vectors a and b using the specified metric."""
    metric_class = get_distance_metric(metric_name)
    metric_instance = metric_class()
    return metric_instance.compute(a, b)
