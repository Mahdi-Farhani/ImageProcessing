# Frequency-Domain Transforms

This document provides a comprehensive guide to frequency-domain image transformations. These transforms analyze and manipulate images in the frequency domain rather than the spatial domain, enabling powerful filtering, analysis, and enhancement operations.

## Table of Contents

1. [Overview](#overview)
2. [Fundamental Concepts](#fundamental-concepts)
3. [Frequency-Domain Transforms](#frequency-domain-transforms)
4. [Implementation Details](#implementation-details)
5. [Behavioral Characteristics](#behavioral-characteristics)
6. [Use Cases](#use-cases)
7. [Performance & Optimization](#performance--optimization)

---

## Overview

Frequency-domain transforms decompose an image into its frequency components, revealing patterns invisible in the spatial domain. Instead of analyzing pixel values directly, we analyze the distribution of different frequencies (how rapidly pixel values change across the image).

**Key Insight:** Many image processing tasks become simpler in the frequency domain:
- Filtering (removing noise, edge detection) → multiplication
- Compression (removing high frequencies) → thresholding
- Analysis (detecting patterns, textures) → spectral analysis

---

## Fundamental Concepts

### Spatial Domain vs. Frequency Domain

| Aspect | Spatial Domain | Frequency Domain |
|--------|---|---|
| **What we see** | Pixel values (brightness) | Magnitude and phase of frequency components |
| **Operations** | Convolution (slow) | Multiplication (fast) |
| **Intuition** | How bright is pixel (x,y)? | How much of frequency f is in the image? |
| **Good for** | Display, direct manipulation | Filtering, compression, analysis |

### Frequency in Images

- **Low Frequencies** — Slow changes in pixel values; represent overall structure, large objects, smooth regions
- **High Frequencies** — Rapid changes; represent edges, details, noise, fine textures
- **Zero Frequency (DC Component)** — Average pixel value (brightness) of the image

### The Fourier Transform

The Fourier Transform decomposes an image into sine and cosine waves of different frequencies:

$$\text{Image} = \sum_{u,v} \text{Magnitude}(u,v) \cdot \cos(\phi(u,v)) + \text{Phase}(u,v)$$

For 2D images, we use the **2D Discrete Fourier Transform (DFT)**:

$$F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cdot e^{-j2\pi(ux/M + vy/N)}$$

Where:
- $F(u,v)$ — Frequency component at coordinate (u,v)
- $f(x,y)$ — Pixel value at spatial coordinate (x,y)
- $M, N$ — Image dimensions

---

## Frequency-Domain Transforms

### 1. Fourier Transform (FFT)

**Behavior:** Decomposes image into frequency components (magnitude and phase).

**Implementation:**
```python
import numpy as np

class FourierTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply Fourier transformation to the input data."""
        # Compute 2D FFT
        f_transform = np.fft.fft2(data)
        
        # Shift zero-frequency component to center for visualization
        f_shifted = np.fft.fftshift(f_transform)
        
        # Compute magnitude spectrum in log scale
        magnitude_spectrum = 20 * np.log(np.abs(f_shifted) + 1)
        
        return np.array(magnitude_spectrum, dtype=np.uint8)
```

**Key Operations:**
- `np.fft.fft2(data)` — Compute 2D FFT
- `np.fft.fftshift()` — Move zero-frequency to center (for visualization)
- `np.abs()` — Extract magnitude
- `np.angle()` — Extract phase
- `20*log()` — Convert to logarithmic scale (reveals subtle details)

**Output:**
- **Magnitude Spectrum** — Shows strength of each frequency component
- **Phase Spectrum** — Shows phase information (often less visually useful)

**Properties:**
- Symmetric for real-valued images
- Zero-frequency (DC) component at center after shift
- Distance from center correlates with frequency (higher distance = higher frequency)

**Performance:**
- Time complexity: O(n log n) where n = number of pixels (via FFT algorithm)
- Much faster than spatial domain convolution for large kernels
- Requires padding for circular convolution

---

### 2. Discrete Cosine Transform (DCT)

**Behavior:** Similar to FFT but uses only cosine basis functions (no sine/imaginary components).

**Advantages over FFT:**
- Real-valued output (easier to interpret)
- Better energy compaction (most information in few coefficients)
- Foundation of JPEG compression
- No phase information needed

**Mathematical Formula:**
$$DCT(u,v) = \alpha(u)\alpha(v) \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cos\left(\frac{\pi(2x+1)u}{2M}\right) \cos\left(\frac{\pi(2y+1)v}{2N}\right)$$

**Implementation (planned):**
```python
class DCTTransform(TransformBase):
    def apply(self, data: np.ndarray) -> np.ndarray:
        """Apply DCT transformation."""
        from scipy.fftpack import dct
        dct_result = dct(dct(data, axis=0), axis=1)
        # Normalize and scale for visualization
        magnitude = np.abs(dct_result)
        magnitude = 20 * np.log(magnitude + 1)
        return np.clip(magnitude, 0, 255).astype(np.uint8)
```

**Use Cases:**
- Image compression (JPEG)
- Feature extraction
- Watermarking
- Denoising via coefficient thresholding

---

### 3. Frequency-Domain Filtering

**Concept:** Multiply frequency spectrum by a filter function to remove/enhance specific frequencies.

#### Low-Pass Filter
**Effect:** Removes high frequencies (blurs image, removes noise/details)

```python
def lowpass_filter(f_shifted, radius):
    """Apply low-pass filter in frequency domain."""
    rows, cols = f_shifted.shape
    crow, ccol = rows // 2, cols // 2
    
    # Create circular mask centered at origin
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    mask = (x*x + y*y <= radius**2).astype(float)
    
    # Apply filter
    f_filtered = f_shifted * mask
    return f_filtered
```

#### High-Pass Filter
**Effect:** Removes low frequencies (enhances edges and details)

```python
def highpass_filter(f_shifted, radius):
    """Apply high-pass filter in frequency domain."""
    rows, cols = f_shifted.shape
    crow, ccol = rows // 2, cols // 2
    
    # Create circular mask
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    mask = (x*x + y*y > radius**2).astype(float)
    
    # Apply filter
    f_filtered = f_shifted * mask
    return f_filtered
```

#### Band-Pass Filter
**Effect:** Preserves only frequencies within a specific range

```python
def bandpass_filter(f_shifted, radius_inner, radius_outer):
    """Apply band-pass filter in frequency domain."""
    rows, cols = f_shifted.shape
    crow, ccol = rows // 2, cols // 2
    
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    r_squared = x*x + y*y
    mask = ((r_squared >= radius_inner**2) & 
            (r_squared <= radius_outer**2)).astype(float)
    
    return f_shifted * mask
```

---

### 4. Inverse Transforms

**Concept:** Convert filtered frequency-domain results back to spatial domain.

```python
def inverse_fourier(f_shifted):
    """Convert filtered frequency domain back to spatial domain."""
    # Shift zero-frequency back to corner
    f_unshifted = np.fft.ifftshift(f_shifted)
    
    # Compute inverse FFT
    spatial_result = np.fft.ifft2(f_unshifted)
    
    # Take magnitude (discard small imaginary components due to rounding)
    result = np.abs(spatial_result)
    
    # Clip and convert to uint8
    return np.clip(result, 0, 255).astype(np.uint8)
```

---

## Behavioral Characteristics

### Magnitude Spectrum Characteristics

1. **Scale:** Use logarithmic scale (20*log) to visualize small and large magnitudes together
   - Without log: bright values dominate, weak details invisible
   - With log: all frequencies visible

2. **Symmetry:** For real-valued images, magnitude spectrum is symmetric around origin
   - Only upper half needed for full information

3. **Zero-Frequency (DC) Component:** Highest peak at center
   - Represents average brightness
   - Often removed before visualization to see other frequencies

### Phase Information

- Contains spatial information (where features are located)
- Critical for reconstruction but less useful for visualization
- Often ignored in simple frequency-domain analysis

---

## Use Cases

### 1. **Noise Removal**
- **Approach:** Apply low-pass filter or wiener filter in frequency domain
- **Advantage:** More effective than spatial filtering for structured noise
- **Example:** Remove periodic interference patterns

### 2. **Edge Detection**
- **Approach:** Apply high-pass filter
- **Effect:** Removes low-frequency (smooth) components, enhances boundaries
- **Result:** Similar to Sobel/Laplacian but more uniform

### 3. **Image Sharpening**
- **Approach:** Enhance high frequencies
- **Example:** `F_enhanced = F + k * (F - F_lowpass)`

### 4. **Deblurring / Restoration**
- **Approach:** Inverse filtering or Wiener filtering
- **Formula:** `H_inv = conj(H) / (|H|^2 + noise_power)`
- **Challenge:** Amplifies noise; requires regularization

### 5. **Compression**
- **Approach:** DCT (JPEG) or frequency thresholding
- **Method:** Keep only coefficients above threshold
- **Benefit:** Removes imperceptible high-frequency details

### 6. **Texture & Pattern Analysis**
- **Approach:** Analyze magnitude spectrum peaks
- **Use:** Detect periodicity, patterns, textures
- **Example:** Detect striped or checkered patterns

### 7. **Watermarking**
- **Approach:** Embed watermark in frequency components
- **Benefit:** Robust to spatial transformations
- **Method:** Modify coefficients in specific frequency bands

### 8. **Image Registration**
- **Approach:** Cross-correlation in frequency domain via FFT
- **Advantage:** O(n log n) complexity vs. O(n²) in spatial domain
- **Use:** Align overlapping images

---

## Performance & Optimization

### Computational Complexity

| Operation | Complexity | Notes |
|-----------|-----------|-------|
| FFT 2D | O(n log n) | n = M×N pixels; much faster than convolution |
| DCT 2D | O(n log n) | Similar to FFT; better energy compaction |
| Spatial convolution | O(n × k²) | n = pixels, k = kernel size |
| Frequency filtering | O(n) | Simple multiplication after FFT |

**Advantage:** Frequency domain wins when kernel/filter is large.

### Optimization Strategies

1. **Padding:** Pad image to power-of-2 dimensions for optimal FFT performance
   ```python
   from scipy.fftpack import next_fast_len
   new_h = next_fast_len(height)
   new_w = next_fast_len(width)
   padded = np.pad(image, ((0, new_h-height), (0, new_w-width)))
   ```

2. **Caching:** Pre-compute filters if reused
   ```python
   filter_kernel = np.fft.fft2(spatial_kernel, s=image.shape)
   # Reuse filter_kernel for multiple images
   ```

3. **GPU Acceleration:** Use CUDA-accelerated FFT (cuFFT) for large images
   ```python
   import cupy as cp
   f_transform = cp.fft.fft2(cp.asarray(image))
   ```

4. **Streaming/Tiling:** For very large images, process in tiles
   ```python
   tile_h, tile_w = 512, 512
   # Process overlapping tiles with smooth blending
   ```

---

## Example Workflow

### Complete Low-Pass Filtering Pipeline

```python
import numpy as np
from core.transform.frequency import FourierTransform

def lowpass_filter_pipeline(image, radius=30):
    """Apply low-pass filter to reduce noise."""
    
    # 1. Compute FFT
    f_transform = np.fft.fft2(image)
    f_shifted = np.fft.fftshift(f_transform)
    
    # 2. Create low-pass filter
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2
    y, x = np.ogrid[-crow:rows-crow, -ccol:cols-ccol]
    mask = (x*x + y*y <= radius**2).astype(float)
    
    # 3. Apply filter
    f_filtered = f_shifted * mask
    
    # 4. Inverse transform
    f_unshifted = np.fft.ifftshift(f_filtered)
    spatial_result = np.fft.ifft2(f_unshifted)
    result = np.abs(spatial_result)
    
    return np.clip(result, 0, 255).astype(np.uint8)

# Usage
from core.utils.image import ImageCoreUtility

image_pil, rgb, gray = ImageCoreUtility.load_image('input.jpg')
filtered = lowpass_filter_pipeline(gray, radius=30)
ImageCoreUtility.save_image(filtered, 'filtered.jpg')
```

---

## Common Pitfalls & Solutions

| Problem | Cause | Solution |
|---------|-------|----------|
| All black output | Not scaling magnitude correctly | Use log scale: `20*log(abs(F)+1)` |
| Artifacts at edges | Image boundaries don't wrap | Pad with zeros or replicate edges |
| Slow FFT | Image dimensions not optimal | Pad to next power-of-2 or use `next_fast_len()` |
| Reconstruction fails | Phase information lost | Keep both magnitude and phase, or don't discard phase |
| Noise amplification | Inverse filtering without regularization | Use Wiener filter or Tikhonov regularization |

---

## Future Enhancements

- [ ] Implement DCT and inverse DCT transforms
- [ ] Add frequency-domain filter presets (Butterworth, Gaussian)
- [ ] Wiener filter for deblurring
- [ ] Fourier-based image registration
- [ ] Phase vocoder for time-scale modification
- [ ] Frequency-domain texture synthesis
- [ ] GPU-accelerated FFT with CuPy
- [ ] Visualization tools for magnitude/phase spectra

---

## References & Resources

- **Fundamental Reading:**
  - Gonzalez & Woods: *Digital Image Processing*
  - Numpy FFT documentation: https://numpy.org/doc/stable/reference/fft.html
  
- **Advanced Topics:**
  - Wiener filtering, constrained least-squares restoration
  - Image registration via phase correlation
  - Frequency-based super-resolution

