from .euclidean import EuclideanDistance

_METRICS = {
    "euclidean": EuclideanDistance,
}

def get_distance_metric(name: str):
    """Retrieve a distance metric class by name."""
    metric_class = _METRICS.get(name.lower())
    if metric_class is None:
        raise ValueError(f"Distance metric '{name}' is not registered.")
    return metric_class