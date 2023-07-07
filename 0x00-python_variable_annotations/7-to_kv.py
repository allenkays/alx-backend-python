#!/usr/bin/env python3
"""
This module provides a function to create tuples with a string
and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string and the square of an int or float.

    Args:
        k: The string element of the tuple.
        v: The int or float element of the tuple.

    Returns:
        A tuple containing the string k and the square of v as a float.
    """
    return k, float(v ** 2)
