import sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(ROOT)


from core.transform import api as T
from core.utils.image import ImageCoreUtility as image 
from core.utils.misc import GeneralUtility as GU    

import numpy as np  
import matplotlib.pyplot as plt


# Load the image
imagePath=GU.UserInput("Enter image path (default: /datasets/BSDS300/images/train/61060.jpg): ",f"{ROOT}/datasets/BSDS300/images/train/61060.jpg")
colorImage,rgb,gray = image.load_image(imagePath)

# Apply Exponential Transformation
exponentialTransform = T.apply_transform(gray, "exponential")

# Display Results
plt.figure(figsize=(10, 3))

plt.subplot(1, 3,1);plt.title("Original Image");plt.imshow(rgb.astype(np.uint8));plt.axis('off')
plt.subplot(1, 3,2);plt.title("Grayscale Image");plt.imshow(gray, cmap='gray');plt.axis('off')
plt.subplot(1, 3,3);plt.title("exponential transform");plt.imshow(exponentialTransform.astype(np.uint8), cmap='gray');plt.axis('off')

plt.tight_layout()
plt.savefig("exponential_transform_result.png")
plt.show()











