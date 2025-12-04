# Distance Metrics

This module contains implementations of various distance metrics used in image processing, machine learning, and pattern recognition.

## Contents
- ✔️ Euclidean distance
- ✔️ Manhattan distance
- ✔️ Chess-board distance
- ❌ Chebyshev distance
- ❌ Minkowski distance
- ❌ Cosine distance
- ❌ Hamming distance

Each metric is implemented in its own file for modularity, while a unified API is provided in `api.py` for simple usage.

## Example
```
from ipplayground.core.distance.api import distance
d = compute("euclidean", [1,2,3], [4,5,6])
p = distance("euclidean", 3,2,4,1)
print(d)
````
