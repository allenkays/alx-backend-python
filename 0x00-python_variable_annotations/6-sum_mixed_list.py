#!/usr/bin/env python3
"""
This module provides a function to return a sum of a mixed floats and ints
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of integers and floats in a mixed list.

    Args:
        mxd_lst: A list containing integers and floats.

    Returns:
        The sum of the integers and floats as a float.
    """
    return float(sum(mxd_lst))
