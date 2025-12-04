# Linear Intensity Transforms

This document describes the behavior and practical use of common linear intensity transforms. Linear transforms are simple point-wise operations that modify pixel values using a linear relationship: output = a * input + b. They are widely used for basic enhancement, normalization, and quick adjustments.

Common Linear Transforms

- Negative (Inversion)
  - Behavior: Inverts pixel intensities.
  - Formula: output = max_value - input (for 8-bit images max_value = 255).
  - Effect: Dark areas become bright and vice versa — useful for photographic negatives, certain feature enhancement tasks and artistic effects.
  - Notes: Works on grayscale or per-channel for color images.

- Brightness Adjustment (Offset)
  - Behavior: Adds a constant offset to every pixel.
  - Formula: output = input + b
  - Effect: Moves the histogram left or right; positive `b` brightens, negative `b` darkens.
  - Implementation notes: Convert to signed/float type when adding, then clip to valid range (e.g., [0,255]).
  - Typical parameter: `b` in range [-255, 255] for 8-bit images.

- Contrast Scaling (Gain)
  - Behavior: Scales pixel values by a constant factor.
  - Formula: output = a * input
  - Effect: `a > 1` increases contrast (stretches values away from midtones); `0 < a < 1` reduces contrast.
  - Implementation notes: Often combined with offset to keep midtones centered: output = a * (input - 128) + 128
  - Typical parameter: `a` > 0 (e.g., 0.5 - 2.0)

- Linear Rescaling (Normalization)
  - Behavior: Maps an input range [min_in, max_in] to an output range [min_out, max_out].
  - Formula: output = (input - min_in) * (max_out - min_out) / (max_in - min_in) + min_out
  - Effect: Stretches or compresses the histogram to use full dynamic range or match a desired range.
  - Use cases: Contrast stretching, preparing images for downstream algorithms.

Behavioral and Implementation Notes

- These transforms are point-wise: each output pixel depends only on the corresponding input pixel. They do not alter spatial relationships or neighborhood information.
- Always consider data type: perform arithmetic in `float32` or `int32` to avoid overflow, then clip and convert to `uint8` when appropriate.
- Clipping is essential: after applying linear operations, clamp values to the valid range (e.g., [0,255]) to prevent wraparound.
- Combine transforms: brightness and contrast adjustments are commonly combined in a single linear expression: `output = a * input + b`.
- Performance: these operations are O(n) (n = number of pixels) and are efficiently implemented using NumPy vectorized operations.

Examples (pseudo-code)

- Negative: `result = 255 - image`
- Brightness: `result = np.clip(image.astype(np.int16) + 30, 0, 255).astype(np.uint8)`
- Contrast: `result = np.clip(1.2 * (image - 128) + 128, 0, 255).astype(np.uint8)`
- Linear rescale: `result = np.clip((image - min_in) * (255/(max_in-min_in)), 0, 255).astype(np.uint8)`

When to use

- Quick corrections (brightness/contrast)
- Preparing images for visualization
- Baseline data augmentation
- Simple normalization steps before more complex processing
