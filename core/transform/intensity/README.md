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
- ✔️ Log Transform
- ✔️ Exponential Transform
- ❌ Power-Law (Gamma) Transform
- ❌ Sigmoid / S-curve Transform
- ❌ Piecewise Linear Transform

1.3 Histogram-Based Intensity Transforms 
- ❌ Histogram Equalization
- ❌ Adaptive Histogram Equalization (CLAHE)
- ❌ Histogram Matching

## Samples
**Negative Transform Sample**
![Negative Transform](/samples/transform/linear/negative_transform_result.png)

*The Negative Transform inverts the intensity of each pixel, producing a photographic negative effect where dark areas become light and light areas become dark.*

**Brightness Adjustment Sample**
_Sample coming soon._

**Contrast Scaling Sample**
_Sample coming soon._

**Linear Intensity Rescaling Sample**
_Sample coming soon._

**Log Transform Sample**
![Log Transform](/samples/transform/non_linear/log_transform_result.png)

*The Log Transform enhances details in dark regions by expanding low‑intensity values while compressing high‑intensity ranges, making subtle shadow information more visible and reducing extreme highlights.*

**Exponential Transform Sample**
![Exponential Transform](/samples/transform/non_linear/exponential_transform_result.png)

*The Exponential Transform amplifies high‑intensity values while compressing darker regions, producing stronger highlights and emphasizing bright details in images with light‑dominant structures.*

**Power-Law (Gamma) Transform Sample**
_Sample coming soon._

**Sigmoid / S-curve Transform Sample**
_Sample coming soon._

**Piecewise Linear Transform Sample**
_Sample coming soon._

**Histogram Equalization Sample**
_Sample coming soon._

**Adaptive Histogram Equalization (CLAHE) Sample**
_Sample coming soon._

**Histogram Matching Sample**
_Sample coming soon._


