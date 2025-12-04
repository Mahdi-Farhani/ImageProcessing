# Image Transform Module

This module provides a clean, unified, and extensible framework for performing various image transformations within the Image Processing Playground project.

All transforms follow a consistent architecture based on a base class (an abstract class that defines the common interface for all transforms), a central registry (a system that keeps track of available transforms and allows dynamic registration), and a minimal API for applying transformations on images.

The goal is to make it easy to expand the system with new types of image transformations, while keeping usage simple and predictable.
---
## 1. Module Overview
Image transforms are operations that modify the pixel values or structure of an image, such as enhancing contrast, adjusting colors, rotating, resizing, or filtering to extract features or improve visual quality.

They may operate on:

- Intensity values (pixel brightness)
- Color channels
- Geometric structure
- Spatial or frequency domains
This module organizes all transform types into logical categories—such as intensity, color, geometric, and domain transforms (see Section 2: Transform Categories)—while maintaining a uniform programming interface.

## 2. Transform Categories

### 2.1 Intensity Transforms
Transformations that operate directly on pixel intensity values (gray or luminance space).

**Linear Intensity Transforms**
- Negative Transform 
- Brightness Adjustment
- Contrast Scaling 
- Linear Rescaling 

**Nonlinear Intensity Transforms**
- Log Transform
- Power‑Law (Gamma)
- Sigmoid / S‑curve
- Piecewise Linear

**Histogram-Based Transforms**
- Histogram Equalization
- Adaptive Histogram Equalization (CLAHE)
- Histogram Matching

### 2.2 Color Transforms 

Operations that modify or convert color channels, such as:

- RGB to Gray scale / Gray scale to RGB ([core/utils/color.py](../utils/color.py): Provides functions for color space conversion between RGB and gray scale.)
- Channel manipulation
- Color balancing


### 2.3 Geometric Transforms 
Operations that change image structure:

- Scaling
- Rotation
- Translation
- Affine / perspective transforms

### 2.4 Frequency-Domain Transforms 
Transforms based on Fourier or cosine domain:

- DFT / FFT transforms
- DCT
- Spectrum filtering
- Frequency masking

---
## Example Usage
Applying the Negative Transform:

```
from core.transform.intensity import api as T
from core.utils.image import ImageCoreUtility

img_color, rgb, gray = ImageCoreUtility.load_image("input.jpg")

# Apply transform
output = T.apply("negative", rgb)

ImageCoreUtility.save_image("negative.jpg", output)

```

---
# Summary
The Transform Module provides:

- A clean and modular architecture
- Unified API for all transform types
- Implementation of the first linear intensity transform (Negative) in [core/transform/intensity/negative.py](intensity/negative.py)
- A clear roadmap for expanding into color, geometric, and frequency transforms
- Planned upcoming features include support for advanced color transforms, geometric operations (scaling, rotation, affine), and frequency-domain processing (FFT, DCT), making the module suitable for a wide range of imaging workflows.