#!/usr/bin/env python3
"""
This module provides a function to return the sum of a list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list: The input list of floating-point numbers.

    Returns:
        The sum of the numbers as a floating-point number.
    """
    return sum(input_list)
