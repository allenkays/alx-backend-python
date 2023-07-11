#!/usr/bin/env python3

"""
This module provides a coroutine that measures runtime.
"""

import asyncio
import time
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and
    returns total_time / n.

    Args:
        n (int): Number of times to run the wait_n routine.
        max_delay (int): Maximum delay in seconds for each
        wait_random coroutine

    Returns:
        float: Average execution time per run.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
