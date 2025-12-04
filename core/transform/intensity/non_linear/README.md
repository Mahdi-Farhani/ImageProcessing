# Nonlinear Intensity Transforms

Nonlinear intensity transforms apply nonlinear functions to pixel values. These operations change the relationship between input and output values in ways that linear transforms cannot, allowing for dynamic range compression/expansion, perceptual adjustments, and more sophisticated tone mapping.

Common Nonlinear Transforms

- Log Transform
  - Behavior: Compresses high-intensity values and expands low-intensity values.
  - Formula: output = c * log(1 + input)
  - Effect: Useful when an image has a large dynamic range — brings out details in dark regions while compressing highlights.
  - Parameter: `c` is a scaling constant that maps the log result back into the desired output range.
  - Implementation notes: Normalize input to a positive domain (e.g., [0,1] or [0,255]) before applying log; convert to float to avoid numerical issues.

- Power-Law (Gamma) Transform
  - Behavior: Applies a power (exponent) to pixel values.
  - Formula: output = c * input**gamma
  - Effect:
    - `gamma < 1` brightens midtones and shadows (useful for monitor display corrections).
    - `gamma > 1` darkens midtones.
  - Use cases: Gamma correction, display linearization, photographic tone adjustments.
  - Implementation notes: Inputs are typically normalized to [0,1] before applying power; scale back to the desired output range afterwards.

- Sigmoid / S‑Curve Transform
  - Behavior: Smooth S-shaped curve that increases contrast in midtones while compressing highlights and shadows.
  - Typical formula (logistic): output = 1 / (1 + exp(-k*(input - x0)))
  - Effect: Enhances local contrast around midtones without clipping extremes; widely used in tone mapping and filmic look adjustments.
  - Parameters: `k` (steepness), `x0` (midpoint)
  - Implementation notes: Normalize input values, tune `k` and `x0` for desired curve.

- Piecewise Linear / Thresholded Transforms
  - Behavior: Apply different linear functions to different ranges of pixel values.
  - Effect: Allows fine-grained control — e.g., boost shadows more than highlights or create posterization effects.
  - Use cases: Local contrast enhancement, stylized effects, adaptive contrast.
  - Implementation notes: Ensure continuity at segment boundaries if required.

- Histogram-Based (Related Nonlinear Methods)
  - Histogram Equalization
    - Behavior: Remap intensity values to flatten the image histogram (increase global contrast).
    - Effect: Makes image details more uniformly visible across intensities.
  - Adaptive Histogram Equalization (CLAHE)
    - Behavior: Apply histogram equalization locally to tiles and clip contrast amplification.
    - Effect: Preserves local contrast without over-amplifying noise.
  - Histogram Matching
    - Behavior: Modify an image's histogram so it matches a reference image's histogram.

Behavioral and Implementation Notes

- Nonlinear transforms often require normalization to a consistent input range (e.g., [0,1]) to avoid numerical instability.
- Use lookup tables (LUTs) for performance when the mapping is static — compute the mapping once and apply it to all pixels.
- Be mindful of rounding and quantization when converting back to integer types — apply dithering if necessary to reduce banding.
- Some nonlinear transforms (like gamma) are invertible given parameters; others (like histogram equalization) are not strictly invertible.
- Many nonlinear transforms change perceived contrast and color balance; when applying to color images, operate on luminance/value channel where appropriate (e.g., convert to HSV/LAB and modify `V`/`L` channel).

Examples (pseudo-code)

- Log (normalized):
  - `x = image.astype(np.float32) / 255.0`
  - `result = c * np.log1p(x)`
  - `result = np.clip(result * 255.0, 0, 255).astype(np.uint8)`

- Gamma (normalized):
  - `x = (image.astype(np.float32) / 255.0)`
  - `result = np.clip((x ** gamma) * 255.0, 0, 255).astype(np.uint8)`

- Sigmoid (normalized):
  - `x = image.astype(np.float32) / 255.0`
  - `result = 1.0 / (1.0 + np.exp(-k*(x - x0)))`
  - `result = np.clip(result * 255.0, 0, 255).astype(np.uint8)`

When to use

- Log: Images with large dynamic range where details in shadows are needed.
- Gamma: Correct display characteristics or artistically adjust midtones.
- Sigmoid: Boost midtone contrast while preserving highlights/shadows.
- Piecewise: Precise local control of tonal mapping; stylized effects.
- Histogram methods: Global or local contrast enhancement, matching image appearance to a target.

