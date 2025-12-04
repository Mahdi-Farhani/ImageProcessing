## Distance Metrics

This document describes the mathematical definitions, use cases, and implementation notes for all available distance metrics in this project.

Each metric is implemented as a class under:

```
src/ipplayground/core/distance/
```

Metrics marked with ✔️ are already implemented.

---

**1. Euclidean Distance ✔️**

Definition:
```
d(a, b) = sqrt( Σ (ai – bi)^2 )
```

Properties:
- L2 norm
- Most common distance function in numerical analysis
- Sensitive to scale

Applications:

- feature comparison
- Image patch matching
- SOM Best Matching Unit (BMU)

---
**2. Manhattan Distance ✔️**

Definition:
```
d(a, b) = Σ |ai – bi|
```
Properties:

- L1 norm
- More robust to outliers

Applications:

- Texture vectors
- Histogram differences
---

**3. Chebyshev Distance (Chessboard) ✔️**
definition:
```
d(a, b) = max |ai – bi|
```

Notes:

- Also known as L∞ norm
- Equivalent to pixel movement on a chessboard (king moves)

**4. Minkowski Distance ✔️**
Definition:
```
d(a, b) = ( Σ |ai – bi|^p )^(1/p)
```

Generalization:

- p=1 → Manhattan
- p=2 → Euclidean
- p→∞ → Chebyshev

Implementation Detail:

Parameter p is passed to the constructor.

---

**5. Cosine Distance ✔️**
Definition:
```
d(a, b) = 1 – (a · b) / (||a|| ||b||)
```

Applications:

- Feature embeddings
- Document vectors
- Normalized image descriptors

---

**6. Hamming Distance ✔️**

Definition:

The number of positions where two vectors differ.

Notes:

- Works on binary or categorical vectors
- Common in hash-based representations
