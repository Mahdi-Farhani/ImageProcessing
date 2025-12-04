## Examples and usages
This document collects example usages for all modules of the project.

To keep the document scalable as new modules are added, examples are organized into clearly separated sections.

index:

- [distance](#distance)

### Distance
Distance metrics are exposed through a unified API based on the Strategy Pattern.

All distance algorithms—regardless of their internal implementation—are accessed through a single entry point:
```
from core.distances import api as dist_api
```
Inputs a and b can be Python lists or NumPy arrays.

The function automatically handles validation and computation.

**Example: Euclidean distance**
```
result = dist_api.compute(a, b, "euclidean")
print(result)
```

