import numpy as np
from .registry import get_transformer

def getInstance(transform_name: str) -> object:
    """Retrieve an instance of a transformer by name."""
    transformer_class = get_transformer(transform_name)
    match transform_name.lower():
        case "scaling":
            return transformer_class(factor=2.0)  # Default factor=2.0 for Scaling
        case _:
            return transformer_class()
def apply_transform(data: np.ndarray, transform_name: str) -> np.ndarray:
    """Apply the specified transformation to the input data."""
    transformer_instance = getInstance(transform_name)
    return transformer_instance.apply(data)    
