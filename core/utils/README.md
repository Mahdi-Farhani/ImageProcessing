# Core Utils Module

The `utils` module provides essential utility functions and classes for image processing tasks, including color space conversions, image I/O operations, and general input handling utilities.

## Overview

This module is organized into three main components:

- **color.py** - Color space conversion utilities
- **image.py** - Image loading and saving utilities
- **misc.py** - General utility functions

## Components

### 1. Color Utilities (`color.py`)

Provides color space conversion functions for image manipulation.

#### `ColorImageUtility`

A utility class for color space transformations.

**Methods:**

- `rgb_to_grayscale(image: np.ndarray) -> np.ndarray`
  - Converts an RGB image to grayscale using the standard luminosity formula
  - Formula: `Gray = 0.2989*R + 0.5870*G + 0.1140*B`
  - **Parameters:**
    - `image` (np.ndarray): RGB image array with shape (height, width, 3)
  - **Returns:** Grayscale image array with shape (height, width)
  - **Raises:** ValueError if input is not a valid RGB image (must have 3 channels)

**Example:**
```python
from core.utils.color import ColorImageUtility
import numpy as np

rgb_image = np.array([[[255, 0, 0]]])  # Red pixel
gray_image = ColorImageUtility.rgb_to_grayscale(rgb_image)
```

---

### 2. Image Utilities (`image.py`)

Handles image loading and saving operations with optional color space conversions.

#### `ImageCoreUtility`

A utility class for image I/O operations.

**Methods:**

- `load_image(path: str, grayscale: bool) -> np.ndarray`
  - Loads an image from disk and optionally converts it to grayscale
  - **Parameters:**
    - `path` (str): Path to the image file
    - `grayscale` (bool): If True, converts the loaded image to grayscale
  - **Returns:** NumPy array representing the image
  - **Dependencies:** Uses `ColorImageUtility.rgb_to_grayscale()` for conversion

- `load_image(path: str) -> tuple`
  - Loads an image and returns multiple representations
  - **Parameters:**
    - `path` (str): Path to the image file
  - **Returns:** Tuple of (PIL Image, RGB numpy array, Grayscale numpy array)

- `save_image(image_array: np.ndarray, path: str) -> None`
  - Saves a NumPy array as an image to the specified path
  - **Parameters:**
    - `image_array` (np.ndarray): Image data to save
    - `path` (str): Output file path
  - **Returns:** None

**Example:**
```python
from core.utils.image import ImageCoreUtility

# Load and convert to grayscale
gray_image = ImageCoreUtility.load_image('image.jpg', grayscale=True)

# Load with multiple representations
pil_img, rgb_array, gray_array = ImageCoreUtility.load_image('image.jpg')

# Save an image
ImageCoreUtility.save_image(gray_image, 'output.jpg')
```

---

### 3. General Utilities (`misc.py`)

Provides general-purpose utility functions.

#### `GeneralUtility`

A utility class for common operations.

**Methods:**

- `UserInput(prompt: str, default: str) -> str`
  - Prompts the user for input and returns the provided value or a default if empty
  - **Parameters:**
    - `prompt` (str): The prompt message to display to the user
    - `default` (str): Default value to return if user input is empty
  - **Returns:** User input string, or the default value if input is blank
  - **Behavior:** Strips whitespace from input before checking if empty

**Example:**
```python
from core.utils.misc import GeneralUtility

user_name = GeneralUtility.UserInput("Enter your name: ", "Anonymous")
```

---

## Dependencies

- **numpy** - Numerical array operations
- **PIL (Pillow)** - Image loading and saving

## Usage in Project

The utilities are commonly imported at the top level as:

```python
from core.utils.color import ColorImageUtility
from core.utils.image import ImageCoreUtility
from core.utils.misc import GeneralUtility
```

Or imported as modules:

```python
from core import utils
# Access as: utils.color.ColorImageUtility, etc.
```

## Integration

These utilities are used throughout the image processing pipeline:

- **distances** module - Uses image utilities for loading test images
- **transform** module - Uses color conversion for intensity transformations
- **samples** - Demonstrates utility usage in example scripts

---

## Future Enhancements

Potential areas for expansion:

- Additional color space conversions (HSV, LAB, etc.)
- Image normalization utilities
- Batch image loading/saving operations
- Image validation and format detection
- Error handling and logging improvements
