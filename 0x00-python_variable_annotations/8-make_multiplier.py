#!/usr/bin/env python3
"""
This module provides a type annotated function that takes a float
multiplier and returns a function that multiplies a float by the
multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The multiplier value.

    Returns:
        A function that takes a float and multiplies it with the multiplier.
    """
    def product(value: float) -> float:
        return value * multiplier

    return product
