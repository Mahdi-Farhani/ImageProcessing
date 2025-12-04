from .euclidean import EuclideanDistance
from .manhattan import ManhattanDistance
from .chess_board import ChessBoardDistance
from .minkowski import MinkowskiDistance
from .cosine import CosineDistance
from .hamming import HammingDistance

_METRICS = {
    "euclidean": EuclideanDistance,
    "manhattan": ManhattanDistance,
    "chessboard": ChessBoardDistance,
    "minkowski": MinkowskiDistance,  # Default p=3 for Minkowski
    "cosine": CosineDistance,
    "hamming": HammingDistance,
}

def get_distance_metric(name: str):
    """Retrieve a distance metric class by name."""
    metric_class = _METRICS.get(name.lower())
    if metric_class is None:
        raise ValueError(f"Distance metric '{name}' is not registered.")
    return metric_class