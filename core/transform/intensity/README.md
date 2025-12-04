# Intensity Transform Module

This module contains transformation functions that operate directly on the intensity values of images. These operations modify pixel brightness levels to enhance contrast, invert intensity, normalize ranges, and build more advanced tone‑mapping steps.

---
## Contents

**1. Intensity Transforms**
Transforms that operate purely on pixel intensity values.

1.1 Linear Intensity Transforms
- ✔️ Negative Transform
- ❌ Brightness Adjustment 
- ❌ Contrast Scaling 
- ❌ Linear Intensity Rescaling 

1.2 Nonlinear Intensity Transforms 
- ❌ Log Transform
- ❌ Power-Law (Gamma) Transform
- ❌ Sigmoid / S-curve Transform
- ❌ Piecewise Linear Transform

1.3 Histogram-Based Intensity Transforms 
- ❌ Histogram Equalization
- ❌ Adaptive Histogram Equalization (CLAHE)
- ❌ Histogram Matching
