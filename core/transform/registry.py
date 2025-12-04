from core.transform.intensity.linear.negative import NegativeTransform
from core.transform.intensity.non_linear.log_transform import LogTransform
from core.transform.frequency.fourier import FourierTransform

_TRANSFORMERS={
    # Intensity Linear Transforms
    "negative": NegativeTransform,
    # Intensity Non-Linear Transforms
    "log": LogTransform,
    # Frequency-Domain Transforms 
    "fourier": FourierTransform,
}

def get_transformer(name: str):
    """Retrieve a transformer class by name."""
    transformer_class = _TRANSFORMERS.get(name.lower())
    if transformer_class is None:
        raise ValueError(f"Transformer '{name}' is not registered.")
    return transformer_class