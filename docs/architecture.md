## Architecture Overview
This document provides a high‑level overview of the internal architecture of the ImageProcessing Playground project.

The goal is to maintain a clean, modular, extensible system suitable for educational exercises and real‑world experimentation.

---
### 1. Project Structure
```
ImageProcessing/
│
├── core/
│   ├── distance/
│   │   ├── base.py
│   │   ├── registry.py
│   │   ├── api.py
│   │   ├── euclidean.py
│   │   ├── manhattan.py
│   │   ├── chebyshev.py
│   │   ├── minkowski.py
│   │   ├── cosine.py
│   │   ├── hamming.py
│   │   └── README.md
│   └── utils/
│
├── samples/
│   └── distance/
│
└── docs/
    ├── architecture.md
    ├── distance-metrics.md
    ├── api-design.md
    ├── examples.md
    └── roadmap.md

```

### 2. Design Principles
**Modularity**
Each distance metric is implemented in its own file.

This enforces separation of concerns and strong encapsulation.

**Strategy Pattern**
The design explicitly follows the Strategy Pattern:

- The base strategy is DistanceMetric
- Each algorithm is a concrete strategy
- The registry routes requests to the correct strategy
- The api provides a unified interface to end‑users
- This ensures uniformity, extensibility, and testability.

**Clean API Surface**
The API exposes one simple compute function:
```
compute(a, b, metric_name, **kwargs)

```
Internals such as registry or class instantiation are hidden from users.

**Extensibility**
Adding a new distance metric requires only:

    1- Implementing a class that inherits from DistanceMetric
    2- Registering it inside registry.py

No modifications to API are necessary for new algorithms.


### 3. Component Responsibilities

**core/distance/base.py**

Defines the abstract base class DistanceMetric.

All algorithms must implement:
```
compute(self, a, b)
distance(self,x,y,s,t)
```

**core/distance/registry.py**

Maintains a mapping from metric name → metric class.

Ensures a plug‑and‑play mechanism for adding new metrics.

**core/distance/api.py**

User-facing API.

Handles parameterization (e.g., Minkowski p-value) and invokes the right metric.

**samples/**
Contains small example scripts demonstrating how to call the API.


