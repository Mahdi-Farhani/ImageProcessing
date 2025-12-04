from core.transform.linear.negative import NegativeTransform


_TRANSFORMERS={
    "negative": NegativeTransform,
}

def get_transformer(name: str):
    """Retrieve a transformer class by name."""
    transformer_class = _TRANSFORMERS.get(name.lower())
    if transformer_class is None:
        raise ValueError(f"Transformer '{name}' is not registered.")
    return transformer_class