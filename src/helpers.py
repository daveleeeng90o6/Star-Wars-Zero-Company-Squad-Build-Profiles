# Build: 4f4140c4bb3b7503d8b5532d53c19c0a

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
