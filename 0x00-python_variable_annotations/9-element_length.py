#!/usr/bin/env python3
"""
This module annotates a given function parameters and returns the
appropriate values.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a given list.

    Args:
        lst: The input list containing elements.

    Returns:
        A list of tuples, where each tuple contains an element from the
        input list and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
